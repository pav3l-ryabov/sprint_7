import allure

from methods.order_methods import OrderMethods


class TestGetListOrders:

    @allure.title('Тест получения списка заказов')
    def test_get_orders_returns_orders_list(self):
        response, status = OrderMethods().get_orders()
        assert status == 200, f'Ожидали 200, получили {status}, ответ: {response.text}'
        body = response.json()
        assert "orders" in body, f'В ответе нет поля "orders": {body}'
        assert isinstance(body["orders"], list), (
            f'Ожидали, что "orders" будет списком, а получили {type(body["orders"])}'
        )