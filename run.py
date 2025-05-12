import asyncio
import os
import sys
import aiohttp
from flexmock import flexmock
import yaml

# has to be before LD imports
try:
    config_path = sys.argv[1]
except IndexError:
    config_path = "./local-config.yaml"
os.environ["LOGDETECTIVE_SERVER_CONF"] = config_path
try:
    output_suffix = sys.argv[2]
except IndexError:
    output_suffix = ""

from logdetective.server.gitlab import generate_mr_comment
from logdetective.server.llm import perform_staged_analysis


def get_logs(file_path = "logs_urls.yaml"):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)  # Use safe_load to prevent arbitrary code execution
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        return None


def get_unique_name(prefix):
    outfile = f"{prefix}.md"
    if not os.path.exists(outfile):
        return outfile
    for i in range(1, 10):
        outfile = f"{prefix}-{i}.md"
        if not os.path.exists(outfile):
            return outfile
    raise RuntimeError()


async def main():
    async with aiohttp.ClientSession() as session:
        for log_dict in get_logs():
            log_url = log_dict["url"]
            name = log_dict["name"]
            print(log_url)
            log_response = await session.get(log_url)
            log_text = await log_response.text()
            staged_response = await perform_staged_analysis(session, log_text=log_text)
            job = flexmock(id="1", project_url="https://gitlab.foobar.baz/", project_name="foo")
            short_comment = await generate_mr_comment(job, log_url, staged_response, full=True)
            outfile = get_unique_name(f"{output_suffix}{name}")
            with open(outfile, "w") as fd:
                fd.write(short_comment)
            # print(short_comment)


asyncio.run(main())