import allure
import requests
import data


class TestOrderBody:

    @allure.title('Test Order Body')
    @allure.description('Тестирование, что в тело ответа возвращается список заказов.')
    def test_order_body(self):
        response = requests.get(f'{data.Url.MAIN_URL}{data.Url.GET_LIST_ORDERS_URL}')
        assert response.json()['orders'][0]['id'] != 0