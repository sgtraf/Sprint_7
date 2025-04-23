import allure
from data import OrderData
from methods.login_method import LoginMethods


class TestLogin:
    @allure.title('Test Successful login')
    @allure.description('Тут создаем логин, входим на сайт, проверяем код ответа')
    def test_courier_authorization(self,get_login_id):
        with allure.step("Создаем курьера"):
            LoginMethods.register_new_courier_and_return_login_password(get_login_id)
        with allure.step("Входим под логином курьера"):
            body = LoginMethods.login_in_system(get_login_id['login'], get_login_id['password'])
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.status_code == 200 and body.json()["id"] != 0

    @allure.title('Test UnSuccessful courier login without necessary data')
    @allure.description('Пытаемся войти без пароля и проверяем ответ API')
    def test_login_courier_without_password(self, get_login_without_password):
        with allure.step("Создаем курьера"):
            LoginMethods.register_new_courier_and_return_login_password(get_login_without_password)
        with allure.step("Пытаемся войти без указания пароля"):
            body_answer_without_pass = LoginMethods.login_in_system(get_login_without_password['login'], '')
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body_answer_without_pass.status_code == 400 and body_answer_without_pass.json()['message'] == OrderData.MESSEGE_INC_LOGIN

    @allure.title('Test Error after login incorrect data')
    @allure.description('Система вернёт ошибку, если неправильно указать логин или пароль;')
    def test_login_with_incorrect_password(self,get_login_with_incorrect_password):
        with allure.step("Создаем курьера"):
            LoginMethods.register_new_courier_and_return_login_password(get_login_with_incorrect_password)
        with allure.step("Пытаемся войти с неправильным паролем"):
            body_answer_withot_pass = LoginMethods.login_in_system(get_login_with_incorrect_password['login'], '4545')
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body_answer_withot_pass.status_code == 404 and body_answer_withot_pass.json()['message'] == OrderData.MESSEGE_NOT_FIND_LOGIN

    @allure.title('Test UnSuccessful courier login without necessary data')
    @allure.description('Если какого-то поля нет, запрос возвращает ошибку')
    def test_login_courier_without_password_error(self, get_login_without_password):
        with allure.step("Создаем курьера"):
            LoginMethods.register_new_courier_and_return_login_password(get_login_without_password)
        with allure.step("Пытаемся войти без указания пароля"):
            body_answer_without_pass = LoginMethods.login_in_system(get_login_without_password['login'], '')
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body_answer_without_pass.status_code == 400 and body_answer_without_pass.json()['message'] == OrderData.MESSEGE_INC_LOGIN

    @allure.title('Test UnSuccessful login with unreal data')
    @allure.description('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_with_unreal_data(self, get_login_with_unreal_data):
        with allure.step("Пытаемся войти с несуществующим пользователем"):
            body = LoginMethods.login_in_system(get_login_with_unreal_data['login'], get_login_with_unreal_data['password'])
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.json()['message'] == OrderData.MESSEGE_NOT_FIND_LOGIN and body.status_code == 404

    @allure.title('Test Successful login return id')
    @allure.description('Успешный запрос возвращает id')
    def test_login_with_real_data(self, get_login_id):
        with allure.step("Создаем курьера"):
            LoginMethods.register_new_courier_and_return_login_password(get_login_id)
        with allure.step("Входим под логином курьера"):
            body = LoginMethods.login_in_system(get_login_id['login'], get_login_id['password'])
        with allure.step("Проверяем, что код ответа и тело соответствует документации"):
            assert body.json()["id"] != 0 and body.status_code == 200
