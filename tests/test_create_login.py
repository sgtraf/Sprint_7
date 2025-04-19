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

    @allure.title('Test UnSuccessful create courier without login data')
    @allure.description('Пытаемся создать курьера без логина и проверяем ответ API')
    def test_create_courier_without_login(self,generate_without_login_data):
        responce = generate_without_login_data
        assert responce.status_code == 400 and responce.json()['message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Test UnSuccessful create courier without password data')
    @allure.description('Пытаемся создать курьера без пароля и проверяем ответ API')
    def test_create_courier_without_password(self, generate_without_password_data):
        responce = generate_without_password_data
        assert responce.status_code == 400 and responce.json()[
            'message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Courier creation returning code 201')
    @allure.description('Проверка, что запрос возвращает правильный код ответа;')
    def test_create_login_ok(self,generate_login_data):
        responce = generate_login_data
        assert responce.status_code == 201

    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "логин", запрос возвращает ошибку;')
    def test_error_create_courier_without_login(self, generate_without_login_data):
        responce = generate_without_login_data
        assert responce.status_code == 400 and responce.json()['message'] == 'Недостаточно данных для создания учетной записи'


    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "пароль", запрос возвращает ошибку;')
    def test_error_create_courier_without_password(self, generate_without_password_data):
        responce = generate_without_password_data
        assert responce.status_code == 400 and responce.json()['message'] == 'Недостаточно данных для создания учетной записи'

