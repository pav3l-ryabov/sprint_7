import requests

from data import BASE_URL, COURIER_URL, COURIER_LOGIN_URL


class CourierMethods:

    def create_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_URL}', json = payload)
        return response, response.status_code

    def login_courier(self, payload):
        response = requests.post(f'{BASE_URL}{COURIER_LOGIN_URL}', json = payload)
        return response, response.status_code

    def delete_courier(self, courier_id):
        response = requests.delete(f'{BASE_URL}{COURIER_URL}/{courier_id}')
        return response, response.status_code

