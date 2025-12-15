import allure
from helpers.order import OrderApi


@allure.feature("Order")
@allure.story("Get orders list")
class TestOrdersList:

    @allure.title("Можно получить список заказов")
    def test_get_orders_list(self):
        response = OrderApi.get_list()

        assert response.status_code == 200

        body = response.json()
        assert "orders" in body
        assert isinstance(body["orders"], list)
