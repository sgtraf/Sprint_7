import allure

class TestLogin:
    @allure.title('Test Successful login')
    @allure.description('Тут создаем логин, входим на сайт, проверяем код ответа')
    def test_courier_authorization(self,get_login_id):
        response = get_login_id
        assert response[1] == 200
