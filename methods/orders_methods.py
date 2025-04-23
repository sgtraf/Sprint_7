import allure
import requests
import urls


class OrdersMethodes:

    @staticmethod
    # метод создания заказа
    def set_order(order):
        with allure.step("Создаем запрос создания заказа"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.CREATE_ORDER_URL}', data=order)
        return response

    @staticmethod
    # метод создания заказа
    def cancel_order(track):
        with allure.step("Создаем запрос отмены заказа"):
            response = requests.put(f'{urls.Url.MAIN_URL}{urls.Url.CANCEL_ORDER_URL}{track}')
        return response
