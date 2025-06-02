import allure

from cart_api import CartAPI
from open_ai import OpenAIClient


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
