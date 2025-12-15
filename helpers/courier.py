# helpers/courier.py
from helpers.api_client import ApiClient

class CourierApi:
    @staticmethod
    def create(payload):
        return ApiClient.post("/api/v1/courier", json=payload)

    @staticmethod
    def login(payload):
        return ApiClient.post("/api/v1/courier/login", json=payload)

    @staticmethod
    def delete(courier_id):
        return ApiClient.delete(f"/api/v1/courier/{courier_id}")
