import allure
from data import OrderData

class TestCreateLogin:
    @allure.title('Test Successful login creation')
    @allure.description('Тут создаем логин и проверяем ответ API')
    def test_create_login(self,generate_login_data):
        response = generate_login_data
        assert response.status_code == 201 and response.json()['ok'] == True

    @allure.title('Test UnSuccessful two login creation with the same data')
    @allure.description('Тут пытаемся создать два курьера с одинаковыми логинами и проверяем ответ API')
    def test_create_two_courier_with_same_data(self, generate_two_courier_with_same_login_data):
        response = generate_two_courier_with_same_login_data
        assert response.status_code == 409 and response.json()['message'] == OrderData.MESSEGE_TEXT_409

    @allure.title('Test UnSuccessful create courier without login data')
    @allure.description('Пытаемся создать курьера без логина и проверяем ответ API')
    def test_create_courier_without_login(self,generate_without_login_data):
        response = generate_without_login_data
        assert response.status_code == 400 and response.json()['message'] == OrderData.MESSEGE_TEXT_400

    @allure.title('Test UnSuccessful create courier without password data')
    @allure.description('Пытаемся создать курьера без пароля и проверяем ответ API')
    def test_create_courier_without_password(self, generate_without_password_data):
        response = generate_without_password_data
        assert response.status_code == 400 and response.json()[
            'message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Courier creation returning code 201')
    @allure.description('Проверка, что запрос возвращает правильный код ответа;')
    def test_create_login_ok(self,generate_login_data):
        response = generate_login_data
        assert response.status_code == 201

    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "логин", запрос возвращает ошибку;')
    def test_error_create_courier_without_login(self, generate_without_login_data):
        response = generate_without_login_data
        assert response.status_code == 400 and response.json()['message'] == OrderData.MESSEGE_TEXT_400

    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "пароль", запрос возвращает ошибку;')
    def test_error_create_courier_without_password(self, generate_without_password_data):
        response = generate_without_password_data
        assert response.status_code == 400 and response.json()['message'] == OrderData.MESSEGE_TEXT_400

    @allure.title('Test UnSuccessful two login creation with the same data')
    @allure.description('Если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_two_courier_with_same_login_data(self, generate_two_courier_with_same_login_data):
        response = generate_two_courier_with_same_login_data
        assert response.status_code == 409 and response.json()['message'] == OrderData.MESSEGE_TEXT_409
