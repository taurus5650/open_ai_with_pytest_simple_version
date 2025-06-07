# Software testing in OpenAI & Pytest

## Article
_to be attached later ..._

## Intro
Integration of OpenAI with Pytest to automate API test generation.

## What You Need to Know and Prepare
- OpenAI Python Library <br>
https://github.com/openai/openai-python
- Pytest (Python testing framework) <br>
https://github.com/pytest-dev/pytest
- API Under Test FakeStoreAPI (Cart endpoint) <br> 
https://fakestoreapi.com/docs#tag/Carts/operation/addCart

# Dev Mode, Deployment, Debug
1. Setup the `OPENAI_API_KEY` at `/deployment/.env`
```commandline
OPENAI_API_KEY=sk-xxxxxxx
```
![OpenApiKey.jpg](readme/OpenApiKey.jpg)

2. Run the command line on terminal.
```commandline
$ make run-docker
```
![MakeRun.jpg](readme/MakeRun.jpg)

3. Run the command line on Docker's terminal.
```commandline
$ pytest -v -s
```

## Result
![AllureResult.png](readme/AllureResult.png)




