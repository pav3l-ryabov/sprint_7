import allure
import pytest

from conftest import create_order_and_cancel
from data import ORDER_ONE_COLOR, ORDER_TWO_COLOR, ORDER_WITHOUT_COLOR


class TestCreateOrder:

    @allure.title('Тест создания заказа с одним, двумя и без цветов')
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_ONE_COLOR,
            ORDER_TWO_COLOR,
            ORDER_WITHOUT_COLOR
        ]
    )
    def test_create_order_with_one_two_without_color(self, order_data, create_order_and_cancel):
        response, status = create_order_and_cancel
        assert status == 201, f'Ожидали 409, получили {status}'
        assert "track" in response.json(), f'В ответе нет поля "track": {response.json()}'


