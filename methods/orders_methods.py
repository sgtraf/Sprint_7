import requests
import data


class OrdersMethodes:

    @staticmethod
    # метод создания заказа
    def set_order(order):
        response = requests.post(f'{data.Url.MAIN_URL}{data.Url.CREATE_ORDER_URL}', data=order)
        return response

    @staticmethod
    # метод создания заказа
    def cancel_order(track):
        response = requests.put(f'{data.Url.MAIN_URL}{data.Url.CANCEL_ORDER_URL}{track}')
        return response
