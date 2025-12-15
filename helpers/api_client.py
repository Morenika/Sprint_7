# helpers/api_client.py
import requests

BASE_URL = "https://qa-scooter.praktikum-services.ru"

class ApiClient:
    @staticmethod
    def post(path, json=None, params=None):
        return requests.post(f"{BASE_URL}{path}", json=json, params=params)

    @staticmethod
    def get(path, params=None):
        return requests.get(f"{BASE_URL}{path}", params=params)

    @staticmethod
    def delete(path, params=None):
        return requests.delete(f"{BASE_URL}{path}", params=params)
