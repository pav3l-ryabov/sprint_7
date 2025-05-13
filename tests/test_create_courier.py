import allure

from conftest import create_courier_and_delete
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title('Тест создания рандомного курьера') # тест, который проверит:
    # что курьера можно создать,
    # успешный запрос возвращает {"ok":true}
    # (проверку добавил внутрь генератора, потому что в нем изначально есть проверка кода ответа и проверка тела ответа не нарушает логику, либо запариваться с отдачей одновременно и кредов и ответа на запрос)
    def test_create_new_random_courier(self, create_courier_and_delete):
        login, password, first_name, _ = create_courier_and_delete
        assert all((login, password, first_name)), \
            'пользователь не создался, т.к. ни одно из полей login, password и firstname не может быть пустым'

    @allure.title('Тест создания двух одинаковых курьеров')
    # тест, который проверит:
    # что нельзя создать двух одинаковых курьеров,
    # запрос возвращает правильный код ответа,
    # если создать пользователя с логином, который уже есть, возвращается ошибка.
    def test_create_double_courier(self, create_courier_and_delete):
        login, password, first_name, _ = create_courier_and_delete
        payload = {"login": login, "password": password, "firstName": first_name}
        response, status = CourierMethods().create_courier(payload)
        assert status == 409, f'Ожидали 409, получили {status}'
        assert response.json() == {'message': 'Этот логин уже используется'}, \
            f'Ожидали сообщение "Этот логин уже используется", получили {response.json}'

    @allure.title('Тест создания курьера без пароля и логина')
    # тест, который проверит:
    # чтобы создать курьера, нужно передать в ручку все обязательные поля
    # если одного из полей нет, запрос возвращает ошибку;
    def test_create_courier_without_login_and_pass(self, create_courier_and_delete):
        login, password, first_name, _ = create_courier_and_delete
        payload = {"login": None, "password": None, "firstName": first_name}
        response, status = CourierMethods().create_courier(payload)
        assert status == 400, f'Ожидали 400, получили {status}'
        assert response.json() == {"message": "Недостаточно данных для создания учетной записи"},\
            f'Ожидали сообщение "Недостаточно данных для создания учетной записи", получили {response.json}'

# Проверь:
# курьера можно создать; done
# нельзя создать двух одинаковых курьеров; done
# чтобы создать курьера, нужно передать в ручку все обязательные поля; done
# запрос возвращает правильный код ответа; done
# успешный запрос возвращает {"ok":true}; done
# если одного из полей нет, запрос возвращает ошибку; done
# если создать пользователя с логином, который уже есть, возвращается ошибка. done