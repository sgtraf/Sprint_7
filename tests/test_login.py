import allure

class TestLogin:
    @allure.title('Test Successful login')
    @allure.description('Тут создаем логин, входим на сайт, проверяем код ответа')
    def test_courier_authorization(self,get_login_id):
        response = get_login_id
        assert response.status_code == 200

    @allure.title('Test UnSuccessful courier login without necessary data')
    @allure.description('Пытаемся войти без пароля и проверяем ответ API')
    def test_login_courier_without_password(self,get_login_withot_password):
        response = get_login_withot_password
        assert response.status_code == 400
