import allure
from data import OrderData
from methods.login_method import LoginMethods


class TestCreateLogin:
    @allure.title('Test Successful login creation')
    @allure.description('Тут создаем логин и проверяем ответ API')
    def test_create_login(self,generate_login_data):
        with allure.step("Создаем курьера"):
            login_body = LoginMethods.register_new_courier_and_return_login_password(generate_login_data)
        with allure.step("Проверяем, что код ответа 201 и тело соответствует документации"):
            assert login_body.status_code == 201 and login_body.json()['ok'] == True

    @allure.title('Test UnSuccessful two login creation with the same data')
    @allure.description('Тут пытаемся создать два курьера с одинаковыми логинами и проверяем ответ API')
    def test_create_two_courier_with_same_data(self, generate_two_courier_with_same_login_data):
        with allure.step("Создаем второго курьера"):
            body = LoginMethods.register_new_courier_and_return_login_password(generate_two_courier_with_same_login_data)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 409 and body.json()['message'] == OrderData.MESSEGE_TEXT_409

    @allure.title('Test UnSuccessful create courier without login data')
    @allure.description('Пытаемся создать курьера без логина и проверяем ответ API')
    def test_create_courier_without_login(self,get_login_with_unreal_data):
        test_body = get_login_with_unreal_data
        test_body['login'] = ''
        with allure.step("Создаем курьера без логина"):
            body = LoginMethods.register_new_courier_and_return_login_password(test_body)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 400 and body.json()['message'] == OrderData.MESSEGE_TEXT_400

    @allure.title('Test UnSuccessful create courier without password data')
    @allure.description('Пытаемся создать курьера без пароля и проверяем ответ API')
    def test_create_courier_without_password(self, get_login_with_unreal_data):
        test_body = get_login_with_unreal_data
        test_body['password'] = ''
        with allure.step("Создаем курьера без пароля"):
            body = LoginMethods.register_new_courier_and_return_login_password(test_body)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 400 and body.json()[
            'message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Courier creation returning code 201')
    @allure.description('Проверка, что запрос возвращает правильный код ответа;')
    def test_create_login_ok(self,generate_login_data):
        with allure.step("Создаем курьера"):
            body = LoginMethods.register_new_courier_and_return_login_password(generate_login_data)
        with allure.step("Проверяем, что код ответа 201 и ответ соответствует документации"):
            assert body.status_code == 201 and body.json()['ok'] == True

    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "логин", запрос возвращает ошибку;')
    def test_error_create_courier_without_login(self, get_login_with_unreal_data):
        test_body = get_login_with_unreal_data
        test_body['login'] = ''
        with allure.step("Создаем курьера без логина"):
            body = LoginMethods.register_new_courier_and_return_login_password(test_body)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 400 and body.json()['message'] == OrderData.MESSEGE_TEXT_400

    @allure.title('Test returning error without some data in body ')
    @allure.description('Если нет поля "пароль", запрос возвращает ошибку;')
    def test_error_create_courier_without_password(self, get_login_with_unreal_data):
        test_body = get_login_with_unreal_data
        test_body['password'] = ''
        with allure.step("Создаем курьера без пароля"):
            body = LoginMethods.register_new_courier_and_return_login_password(test_body)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 400 and body.json()[
            'message'] == 'Недостаточно данных для создания учетной записи'

    @allure.title('Test UnSuccessful two login creation with the same data')
    @allure.description('Если создать пользователя с логином, который уже есть, возвращается ошибка.')
    def test_create_two_courier_with_same_login_data(self, generate_two_courier_with_same_login_data):
        with allure.step("Создаем второго курьера c тем же логином"):
            body = LoginMethods.register_new_courier_and_return_login_password(
                generate_two_courier_with_same_login_data)
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 409 and body.json()['message'] == OrderData.MESSEGE_TEXT_409
