import allure

from data import EXPECTED_NOT_ENOUGH_CREDS, EXPECTED_ACC_NOT_FOUND
from methods.courier_methods import CourierMethods
from conftest import create_courier_and_delete


class TestLoginCourier:

    @allure.title('Тест успешной авторизации курьера') # тест, который проверит:
    # курьер может авторизоваться;
    # успешный запрос возвращает {"ok":true}
    # успешный запрос возвращает id
    def test_create_and_login_courier(self, create_courier_and_delete):
        login, password, _, _ = create_courier_and_delete
        payload = {"login": login, "password": password}
        response, status = CourierMethods().login_courier(payload)
        assert status == 200, f'Ожидали 200, получили {status}'
        assert "id" in response.json(), f'В ответе нет поля "id": {response.json()}'

    @allure.title('Тест авторизации курьера без пароля')
    # тест, который проверит:
    # для авторизации нужно передать все обязательные поля
    # если какого-то поля нет, запрос возвращает ошибку;
    def test_create_and_login_courier_without_pass(self, create_courier_and_delete):
        login, _, _, _ = create_courier_and_delete
        payload = {"login": login, "password": None}
        response, status = CourierMethods().login_courier(payload)
        assert status == 400, f'Ожидали 400, получили {status}'
        assert response.json() == EXPECTED_NOT_ENOUGH_CREDS, \
            f'Ожидали сообщение {EXPECTED_NOT_ENOUGH_CREDS}, а получили {response.json}'

    @allure.title('Тест авторизации существующего курьера с неправильным паролем')
    # тест, который проверит:
    # система вернёт ошибку, если неправильно указать логин или пароль
    def test_create_and_login_courier_with_invalid_pass(self, create_courier_and_delete):
        login, _, _, _ = create_courier_and_delete
        payload = {"login": login, "password": 'invalid_pass'}
        response, status = CourierMethods().login_courier(payload)
        assert status == 404, f'Ожидали 404, получили {status}'
        assert response.json() == EXPECTED_ACC_NOT_FOUND, \
            f'Ожидали сообщение {EXPECTED_ACC_NOT_FOUND}, а получили {response.json}'

    @allure.title('Тест авторизации курьера с несуществующим логином')
    # тест, который проверит:
    # если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
    def test_create_and_login_courier_with_invalid_login(self, create_courier_and_delete):
        _, password, _, _ = create_courier_and_delete
        payload = {"login": 'invalid_login', "password": password}
        response, status = CourierMethods().login_courier(payload)
        assert status == 404, f'Ожидали 404, получили {status}'
        assert response.json() == EXPECTED_ACC_NOT_FOUND, \
            f'Ожидали сообщение {EXPECTED_ACC_NOT_FOUND}, а получили {response.json}'

# Проверь:
# курьер может авторизоваться; done
# для авторизации нужно передать все обязательные поля; done
# система вернёт ошибку, если неправильно указать логин или пароль; done
# если какого-то поля нет, запрос возвращает ошибку; done
# если авторизоваться под несуществующим пользователем, запрос возвращает ошибку; done
# успешный запрос возвращает id. done