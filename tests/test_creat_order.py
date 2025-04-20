import allure
import pytest
import data
from methods.orders_methods import OrdersMethodes


class TestCreateOrder:

    track_code = []

    @allure.title('Test Create Order')
    @allure.description('Тестирование, что можно указать один из цветов — BLACK или GREY; можно указать оба цвета;     можно совсем не указывать цвет;  тело ответа содержит track.')
    @pytest.mark.parametrize('order_number', data.OrderData.ORDERS)
    def test_create_orders(self, order_number):
        response = OrdersMethodes.set_order(order_number)
        self.track_code.append(response.json()['track'])
        assert response.status_code == 201 and response.json()['track'] !=0

    # добавь teardown_class
    # отменяем созданные заказы
    @classmethod
    def teardown_class(cls):
        for i in cls.track_code:
            OrdersMethodes.cancel_order(i)
