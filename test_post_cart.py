from http import HTTPStatus

import allure
from pytest_check import check

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

    @allure.feature('test_post_car_with_ai')
    def test_with_ai(self):
        """ Let OpenAI Build and Verify Basic Test Cases """

        test_cases_str = self.open_ai_client.generate_api_test_cases(
            method=self.PROMPT['method'],
            api_path=self.PROMPT['api_path'],
            request_sample=self.PROMPT['request_sample'],
            response_sample=self.PROMPT['response_sample'],
            max_cases_number=3
        )
        test_cases = self.open_ai_client.parse_ai_response(
            response_str=test_cases_str
        )

        for case in test_cases:
            self.open_ai_client.print_test_cases(
                test_case=case
            )
            input_data = case['input']
            expected_status = case['expected']['status_code']
            expected_response = case['expected']['response']

            resp = self.api.post_cart(
                cartId=input_data['id'],
                userId=input_data['userId'],
                products=input_data.get('products', [])
            )

            assert resp.status_code == HTTPStatus.OK
            res = resp.json()
            check.is_in('userId', res)

            if input_data.get('products'):
                check.equal(res['products'][0]['title'], input_data['products'][0]['title'])
                check.equal(res['products'][0]['category'], input_data['products'][0]['category'])
            else:
                check.equal(res['products'], [])
