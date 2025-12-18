# helpers/courier.py
import allure
from helpers.api_client import ApiClient

class CourierApi:
    @staticmethod
    @allure.step("Create courier")
    def create(payload):
        return ApiClient.post("/api/v1/courier", json=payload)

    @staticmethod
    @allure.step("Login courier")
    def login(payload):
        return ApiClient.post("/api/v1/courier/login", json=payload)

    @staticmethod
    @allure.step("Delete courier (id={courier_id})")
    def delete(courier_id):
        return ApiClient.delete(f"/api/v1/courier/{courier_id}")
