import os
import textwrap

from dotenv import load_dotenv
from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key=None):
        if api_key is None:
            load_dotenv()
            # print('OPENAI_API_KEY:', os.getenv('OPENAI_API_KEY'))
            api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)

    def generate_api_test_cases(
            self, method: str, api_path: str, request_sample: dict, response_sample: dict, resp_err_code: str = None):
        """Setup AI chat content, to generate API test cases."""

        user_prompt_content = textwrap.dedent(
            """
            Please according the API sample to generate test case:
            method: {method}
            api path: {api_path}
            request sample: {request_sample}
            response sample: {request_sample}
            response error code (if have): {resp_err_code}
            """
        ).strip()

        prompt = [
            {
                "role": "system",
                "content": "You're a Senior Software QA Engineer, will in charge designing test cases."
            },
            {
                "role": "user",
                "content": user_prompt_content
            }
        ]
        response = self.client.chat.completions.create(
            model='gpt-4.1-nano',
            messages=prompt,
            temperature=0.3,
            max_tokens=10
        )
        return response.choices[0].message.content
