# Log Detective Model Battleground

This is a comparison of various models that are evauluated on the same log set.
We are generting the full Gitlab MR comment with them.

Right now we have results here from 2 models:
1. [gemma 3](/gemma3-12b/)
2. [gemini 2.5 flash](/gemini-2.5-flash/)
3. [Mistral-7B-Instruct-v0.2/](/Mistral-7B-Instruct-v0.2/)
4. [granite 3.3 8b](/granite-3.3-8b/)

## Usage

Make sure that `logdetective.server` is available on your `$PYTHONPATH` because
the `run.py` script is using functions from it. For gemini I had to do 2 code changes:
1. Comment out all logprobs operations because gemini doesn't implement logprobs
2. Drop the `/v1/` prefix in the URL

```
$ python3 run.py local-config.yaml $dir_with_results
```

Arguments:
1. logdetective server config, one is included in the repo, gemini config is
   below; make sure your inference is running
2. dir where the results should be put (default current working dir)

Sample gemini config:
```
log:
  level_stream: "DEBUG"
  level_file: "DEBUG"
  format: "%(asctime)s - %(levelname)s - %(message)s"
inference:
  max_tokens: 10000
  # log_probs: 1  this doesn't work with gemini openai api
  url: https://generativelanguage.googleapis.com/v1beta/openai
  api_token: abcdef
  model: gemini-2.5-flash-preview-04-17  # gemini-2.5-flash
extractor:
  context: true
  max_clusters: 25
  verbose: false
```
