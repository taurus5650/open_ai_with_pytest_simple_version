import os
import textwrap

from dotenv import load_dotenv
from openai import OpenAI
import json
import json5


class OpenAIClient:
    def __init__(self, api_key=None):
        if api_key is None:
            load_dotenv()
            # print('OPENAI_API_KEY:', os.getenv('OPENAI_API_KEY'))
            api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(
            api_key=api_key,
            base_url='https://api.chatanywhere.tech/v1'
        )

    def parse_ai_response(self, response_str: str):
        # print('AI return response string:', response_str)
        try:
            return json5.loads(response_str)
        except ValueError as e:
            print(f'Cannot decode JSON5: {e}')
            # print('Response string was:', response_str)
            raise

    def generate_api_test_cases(
            self, method: str, api_path: str, request_sample: dict, response_sample: dict, max_cases_number: int,
            max_tokens: int = 1500, resp_err_code: str = None):
        """Setup AI chat content, to generate API test cases."""

        user_prompt_content = textwrap.dedent(f"""
            You are a Senior Software QA Engineer who designs test cases.
            Given the API details below, generate a JSON array of test cases.
            Each test case should have 'input' and 'expected' fields.
            Return ONLY a valid JSON array, without any extra text or explanation.
            Output MUST end with closing square bracket: `]`
            ONLY GENERATE {max_cases_number} CASES

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
            model='gpt-4.1-nano',
            messages=prompt,
            temperature=0.3,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content
