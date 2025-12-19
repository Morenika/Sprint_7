import allure
from helpers.courier import CourierApi


@allure.feature("Courier")
@allure.story("Create courier")
class TestCreateCourier:

    @allure.title("Можно создать курьера: 201 и ok=true")
    def test_create_courier_success(self, courier_data, cleanup_courier):
        response = CourierApi.create(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        cleanup_courier.update(courier_data)

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_duplicate_courier(self, created_courier):
        duplicate_payload = {
            "login": created_courier["login"],
            "password": created_courier["password"],
            "firstName": created_courier["firstName"]
        }

        response = CourierApi.create(duplicate_payload)
        assert response.status_code == 409

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self, courier_data):
        payload = {
            "password": courier_data["password"],
            "firstName": courier_data["firstName"]
        }
        response = CourierApi.create(payload)
        assert response.status_code == 400

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self, courier_data):
        payload = {
            "login": courier_data["login"],
            "firstName": courier_data["firstName"]
        }
        response = CourierApi.create(payload)
        assert response.status_code == 400

