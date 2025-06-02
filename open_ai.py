from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key="xxxx"):
        self.client = OpenAI(api_key=api_key)

    def generate_api_test_cases(self, method: str, api_path: str, request_sample: dict, response_sample: dict):
        prompt = [
            {"role": "system",
             "content": "You're a Senior Software QA Engineer, will in charge designing test case."},
            {"role": "user",
             "content": f"Please according the API sample generate test case: \nmethod: {method}\napi_path: {api_path}\nrequest_sample: {request_sample}\nresponse_sample: {response_sample}"}
        ]
        response = self.client.chat.completions.create(
            model='gpt-4.1-mini',
            messages=prompt,
            temperature=0.3,
            max_tokens=10
        )
        return response.choices[0].message.content
