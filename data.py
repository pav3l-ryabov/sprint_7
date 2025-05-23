BASE_URL = 'http://qa-scooter.praktikum-services.ru/'

COURIER_URL = '/api/v1/courier'
COURIER_LOGIN_URL = '/api/v1/courier/login'

ORDER_URL = '/api/v1/orders'
CANCEL_URL = '/api/v1/orders/cancel'
GET_ORDER_URL = '/api/v1/orders/track'

ORDER_ONE_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}
ORDER_TWO_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK",
        "GREY"
    ]
}
ORDER_WITHOUT_COLOR = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": []
}

EXPECTED_LOGIN_ALREADY_USED = {'message': 'Этот логин уже используется'}
EXPECTED_NOT_ENOUGH_DATA = {"message": "Недостаточно данных для создания учетной записи"}

EXPECTED_NOT_ENOUGH_CREDS = {"message":  "Недостаточно данных для входа"}
EXPECTED_ACC_NOT_FOUND = {"message": "Учетная запись не найдена"}