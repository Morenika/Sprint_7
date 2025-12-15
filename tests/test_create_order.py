import allure
import pytest
from helpers.order import OrderApi


@allure.feature("Order")
@allure.story("Create order")
class TestCreateOrder:

    @allure.title("Создание заказа с разными вариантами цвета")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None
        ]
    )
    def test_create_order_with_different_colors(self, color):
        payload = {
            "firstName": "Natasha",
            "lastName": "Test",
            "address": "Moscow, Test street, 1",
            "metroStation": 1,
            "phone": "+79990000000",
            "rentTime": 1,
            "deliveryDate": "2025-12-20",
            "comment": "test order"
        }

        if color is not None:
            payload["color"] = color

        response = OrderApi.create(payload)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
