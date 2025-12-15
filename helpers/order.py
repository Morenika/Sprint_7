# helpers/order.py
from helpers.api_client import ApiClient

class OrderApi:
    @staticmethod
    def create(payload):
        return ApiClient.post("/api/v1/orders", json=payload)

    @staticmethod
    def get_list():
        return ApiClient.get("/api/v1/orders")
