import allure

from cart_api import CartAPI
from open_ai_client import OpenAIClient


class TestCase:

    api = CartAPI()
    open_ai_client = OpenAIClient()

    PROMPT = {
        "method": "POST",
        "api_path": "/carts",
        "request_sample": {
            "id": 0,
            "userId": 0,
            "products": [
                {
                    "id": 1,
                    "title": "string",
                    "price": 0.1,
                    "description": "string",
                    "category": "string",
                    "image": "http://example.com"
                }
            ]
        },
        "response_sample": {
            "id": 0,
            "userId": 0,
            "products": [
                {
                    "id": 1,
                    "title": "string",
                    "price": 0.1,
                    "description": "string",
                    "category": "string",
                    "image": "http://example.com"
                }
            ]
        },
    }

    @allure.feature('test_with_ai')
    def test_with_ai(self):
        test_cases_str = self.open_ai_client.generate_api_test_cases(
            method=self.PROMPT['method'],
            api_path=self.PROMPT['api_path'],
            request_sample=self.PROMPT['request_sample'],
            response_sample=self.PROMPT['response_sample'],
        )
        test_cases = json.loads(test_cases_str)

        for case in test_cases:
            input_data = case['input']
            expected_status = case['expected']['status_code']
            expected_response = case['expected']['response']

            resp = self.api.post_cart(
                cartId=input_data['cartId'],
                userId=input_data['userId'],
                products=input_data['products']
            )

            assert resp.status_code == expected_status
            assert resp.json() == expected_response
