import requests

from data import BASE_URL, ORDER_URL, CANCEL_URL, GET_ORDER_URL


class OrderMethods:

    def create_order(self, payload):
        response = requests.post(f'{BASE_URL}{ORDER_URL}', json = payload)
        return response, response.status_code

    def get_orders(self):
        response = requests.get(f'{BASE_URL}{ORDER_URL}')
        return response, response.status_code

    def cancel_order(self, payload):
        response = requests.put(f'{BASE_URL}{CANCEL_URL}', json = payload)
        return response, response.status_code