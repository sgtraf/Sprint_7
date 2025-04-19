import allure
from methods.login_method import LoginMethods


class TestCreateLogin:
    @allure.title('Test Successful login creation')
    @allure.description('Тут создаем логин и проверяем ответ API')
    def test_create_login(self,generate_login_data):
        responce = generate_login_data
        assert responce.status_code == 201 and responce.json()['ok'] == True

    @allure.title('Test UnSuccessful two login creation with the same data')
    @allure.description('Тут пытаемся создать два курьера с одинаковыми логинами и проверяем ответ API')
    def test_create_two_courier_with_same_data(self, generate_two_courier_with_same_login):
        responce = generate_two_courier_with_same_login
        assert responce.status_code == 409 and responce.json()['message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Test UnSuccessful create corier without login data')
    @allure.description('Пытаемся создать курьера без логина и проверяем ответ API')
    def test_create_curier_without_login(self,generate_without_login_data):
        responce = generate_without_login_data
        assert responce.status_code == 400 and responce.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Test UnSuccessful create login without some data')
    @allure.description('Пытаемся создать курьера без логина и проверяем ответ API')
    def test_create_curier_without_login(self, generate_without_login_data):
        responce = generate_without_login_data
        assert responce.status_code == 400 and responce.json()[
            'message'] == 'Недостаточно данных для создания учетной записи'
