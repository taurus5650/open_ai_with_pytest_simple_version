from cart_api import CartAPI

class TestCase:

    api = CartAPI()

    def test_something(self):
        resp = self.api.post_cart(
            cartId=1,
            userId=1,
            products=[{"id": 1, "title": "testing"}]
        )