from urllib.parse import urljoin

from request import APIRequest


class CartAPI(APIRequest):
    BASE_URL = 'https://fakestoreapi.com/'
    POST_CART = 'carts'

    def __init__(self, waitingTime=5):
        super().__init__(waiting_time=waitingTime)

    def post_cart(self, cart_id: int, userId: int, products: dict):
        body = {
            "id": cart_id,
            "userId": userId,
            "products": products
        }

        return self._send_request(
            method='POST',
            url=urljoin(self.BASE_URL, self.POST_CART),
            json=body
        )
