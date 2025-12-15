import allure
import pytest
from helpers.courier import CourierApi


@allure.feature("Courier")
@allure.story("Login courier")
class TestLoginCourier:

    @allure.title("Курьер может авторизоваться и получить id")
    def test_login_courier_success(self, created_courier):
        response = CourierApi.login({
            "login": created_courier["login"],
            "password": created_courier["password"]
        })

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при неверном пароле")
    def test_login_with_wrong_password(self, created_courier):
        response = CourierApi.login({
            "login": created_courier["login"],
            "password": "wrong_password"
        })

        assert response.status_code == 404

    @allure.title("Ошибка при отсутствии пароля (нестабильный стенд)")
    @pytest.mark.xfail(reason="Стенд возвращает 504 вместо ошибки", strict=True)
    def test_login_without_password(self, created_courier):
        response = CourierApi.login({
            "login": created_courier["login"]
        })

        assert response.status_code == 400

    @allure.title("Ошибка если не передать логин")
    def test_login_without_login(self, created_courier):
        response = CourierApi.login({
            "password": created_courier["password"]
        })

        assert response.status_code == 400

    @allure.title("Ошибка если авторизоваться под несуществующим пользователем")
    def test_login_nonexistent_user(self):
        response = CourierApi.login({
            "login": "no_such_user_123456",
            "password": "any_pass"
        })

        assert response.status_code == 404
