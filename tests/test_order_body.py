import allure
import requests
import data
from methods.orders_methods import OrdersMethodes


class TestCreateOrder:

    track_code = []

    @allure.title('Test Order Body')
    @allure.description('Тестирование, что в тело ответа возвращается список заказов.')
    def test_create_orders(self):
        response = requests.get(f'{data.Url.MAIN_URL}{data.Url.GET_LIST_ORDERS_URL}')
        assert response.json()['orders'][0]['id'] != 0