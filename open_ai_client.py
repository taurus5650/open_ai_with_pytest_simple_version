import json
import os
import textwrap

import json5
from dotenv import load_dotenv
from openai import OpenAI


class OpenAIClient:
    def __init__(self, api_key=None):
        if api_key is None:
            load_dotenv(dotenv_path='deployment/.env')
            # print('OPENAI_API_KEY:', os.getenv('OPENAI_API_KEY'))
            api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(
            api_key=api_key,
            base_url='https://free.v36.cm/v1/' # https://api.chatanywhere.tech/v1
        )

    def parse_ai_response(self, response_str: str):
        # print('AI return response string:', response_str)
        try:
            return json5.loads(response_str)
        except ValueError as e:
            print(f'Cannot decode JSON5: {e}')
            # print('Response string was:', response_str)
            raise

    def print_test_cases(self, test_case: dict):
        print()
        print('-' * 40)
        print(f"▶ Test case: {test_case.get('test_case_name', 'unnamed')}")
        # print("Input:", json.dumps(test_case['input'], indent=2))
        # print("Expected:", json.dumps(test_case['expected'], indent=2))
        print('-' * 40)

    def generate_api_test_cases(
            self, method: str, api_path: str, request_sample: dict, response_sample: dict, max_cases_number: int,
            max_tokens: int = 1500, resp_err_code: str = None):
        """Setup AI chat content, to generate API test cases."""

        user_prompt_content = textwrap.dedent(f"""
            You're a Senior SDET who designs test cases.
            Given the API details below, generate the test cases.
            Each test case should have 'input' and 'expected' fields.
            Return ONLY a valid JSON array, without any extra text or explanation.
            Output MUST end with closing square bracket: `]`
            ONLY GENERATE P0 CASES, AND {max_cases_number} CASES.

            Method: {method}
            API path: {api_path}
            Request sample: {json.dumps(request_sample, indent=2)}
            Response sample: {json.dumps(response_sample, indent=2)}
            Response error code: {resp_err_code if resp_err_code else 'None'}

            Example output format:
            [
              {{
                "test_case_name": "test_with_valid_products",
                "input": {{ ... }},
                "expected": {{
                  "status_code": 200,
                  "response": {{ ... }}
                }}
              }},
              ...
            ]
        """).strip()

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
            model='gpt-3.5-turbo',
            messages=prompt,
            temperature=0.3,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content

