import allure
from data import OrderData


class TestLogin:
    @allure.title('Test Successful login')
    @allure.description('Тут создаем логин, входим на сайт, проверяем код ответа')
    def test_courier_authorization(self,get_login_id):
        response = get_login_id
        assert response.status_code == 200 and response.json()["id"] != 0

    @allure.title('Test UnSuccessful courier login without necessary data')
    @allure.description('Пытаемся войти без пароля и проверяем ответ API')
    def test_login_courier_without_password(self,get_login_withot_password):
        response = get_login_withot_password
        assert response.status_code == 400 and response.json()['message'] == OrderData.MESSEGE_INC_LOGIN

    @allure.title('Test Error after login incorrect data')
    @allure.description('Система вернёт ошибку, если неправильно указать логин или пароль;')
    def test_login_with_icorrect_password(self,get_login_with_incorrect_password):
        response = get_login_with_incorrect_password
        assert response.status_code == 404 and response.json()['message'] == OrderData.MESSEGE_NOT_FIND_LOGIN

    @allure.title('Test UnSuccessful courier login without necessary data')
    @allure.description('Пытаемся войти без пароля и проверяем ответ API')
    def test_login_courier_without_password(self,get_login_withot_password):
        response = get_login_withot_password
        assert response.json()['message'] == OrderData.MESSEGE_INC_LOGIN and response.status_code == 400

    @allure.title('Test UnSuccessful login with unreal data')
    @allure.description('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_with_unreal_data(self, get_login_with_unreal_data):
        response = get_login_with_unreal_data
        assert response.json()['message'] == OrderData.MESSEGE_NOT_FIND_LOGIN and response.status_code == 404

    @allure.title('Test Successful login return id')
    @allure.description('Успешный запрос возвращает id')
    def test_login_with_unreal_data(self, get_login_id):
        response = get_login_id
        assert response.json()["id"] != 0 and response.status_code == 200
