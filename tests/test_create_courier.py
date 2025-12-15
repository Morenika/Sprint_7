import allure
from helpers.courier import CourierApi


@allure.feature("Courier")
@allure.story("Create courier")
class TestCreateCourier:

    @allure.title("Можно создать курьера: 201 и ok=true")
    def test_create_courier_success(self, courier_data):
        response = CourierApi.create(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух курьеров с одинаковым логином")
    def test_create_duplicate_courier(self, courier_data):
        first_response = CourierApi.create(courier_data)
        second_response = CourierApi.create(courier_data)

        assert first_response.status_code == 201
        assert second_response.status_code == 409

    @allure.title("Нельзя создать курьера без логина")
    def test_create_courier_without_login(self):
        payload = {
            "password": "pass123",
            "firstName": "Test"
        }

        response = CourierApi.create(payload)

        assert response.status_code == 400

    @allure.title("Нельзя создать курьера без пароля")
    def test_create_courier_without_password(self):
        payload = {
            "login": "test_login_no_password",
            "firstName": "Test"
        }

        response = CourierApi.create(payload)

        assert response.status_code == 400
