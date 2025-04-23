import requests
import urls


class OrdersMethodes:

    @staticmethod
    # метод создания заказа
    def set_order(order):
        response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.CREATE_ORDER_URL}', data=order)
        return response

    @staticmethod
    # метод создания заказа
    def cancel_order(track):
        response = requests.put(f'{urls.Url.MAIN_URL}{urls.Url.CANCEL_ORDER_URL}{track}')
        return response
