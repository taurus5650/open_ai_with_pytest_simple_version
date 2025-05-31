from cart_api import CartAPI

class TestCase:

    api = CartAPI()

    def test_something(self):
        resp = self.api.post_cart(
            id=1,
            userId=1,
            prducts=[{"id": 1, "title": "testing"}]
        )