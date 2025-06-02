from openai import OpenAI
import textwrap


class OpenAIClient:
    def __init__(self, api_key="xxxx"):
        self.client = OpenAI(api_key=api_key)

    def generate_api_test_cases(self, method: str, api_path: str, request_sample: dict, response_sample: dict, resp_err_code: str = None):
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
            model='gpt-4.1-mini',
            messages=prompt,
            temperature=0.3,
            max_tokens=10
        )
        return response.choices[0].message.content
