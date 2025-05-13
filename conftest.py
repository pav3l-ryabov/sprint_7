import pytest
import courier_generator

from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def create_courier_and_delete():
    login, password, first_name = courier_generator.register_new_courier_and_return_login_password()
    payload = {"login": login, "password": password}
    response, status = CourierMethods().login_courier(payload)
    assert status == 200, f'Не удалось залогинить курьера, статус: {status}, ответ: {response.json()}'
    courier_id = response.json().get("id")
    assert courier_id is not None, 'ID курьера не найден в ответе'
    yield {
        "login": login,
        "password": password,
        "first_name": first_name,
        "id": courier_id
    }

    CourierMethods().delete_courier(courier_id)

@pytest.fixture
def create_order_and_cancel(order_data):
    response, status = OrderMethods().create_order(order_data)
    track = response.json().get("track")
    assert track is not None, 'track не найден в ответе'
    yield response, status
    OrderMethods().cancel_order(track)