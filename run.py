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


async def main():
    async with aiohttp.ClientSession() as session:
        for log_url in get_logs():
            print(log_url)
            log_response = await session.get(log_url)
            log_text = await log_response.text()
            staged_response = await perform_staged_analysis(session, log_text=log_text)
            job = flexmock(id="1", project_url="https://gitlab.foobar.baz/", project_name="foo")
            short_comment = await generate_mr_comment(job, log_url, staged_response, full=False)
            name_prefix = log_url.rsplit("/", 2)[1]
            with open(f"./{name_prefix}.md", "w") as fd:
                fd.write(short_comment)
            # print(short_comment)


asyncio.run(main())