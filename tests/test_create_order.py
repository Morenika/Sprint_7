import allure
import pytest
from helpers.order import OrderApi

def base_order_payload():
    return {
        "firstName": "Natasha",
        "lastName": "Test",
        "address": "Moscow, Test street, 1",
        "metroStation": 1,
        "phone": "+79990000000",
        "rentTime": 1,
        "deliveryDate": "2025-12-20",
        "comment": "test order"
    }
payload_black = {**base_order_payload(), "color": ["BLACK"]}
payload_grey = {**base_order_payload(), "color": ["GREY"]}
payload_both = {**base_order_payload(), "color": ["BLACK", "GREY"]}
payload_no_color = base_order_payload()  # без поля color

@allure.feature("Order")
@allure.story("Create order")
class TestCreateOrder:

    @allure.title("Создание заказа возвращает track (BLACK/GREY/BOTH/NO_COLOR)")
    @pytest.mark.parametrize("payload", [payload_black, payload_grey, payload_both, payload_no_color])
    def test_create_order_returns_track(self, payload):
        response = OrderApi.create(payload)
        assert response.status_code == 201
        assert "track" in response.json()
