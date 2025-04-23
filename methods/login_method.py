import allure
import requests
import urls


class LoginMethods:

    @staticmethod
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    def register_new_courier_and_return_login_password(body):

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        with allure.step("Создаем запрос создания курьера"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.CREATE_COURIER_URL}', data=body)

        return response

    @staticmethod
    def login_in_system(login, password):
        params = {'login': login, 'password': password}
        with allure.step("Создаем запрос залогинивания курьера"):
            response = requests.post(f'{urls.Url.MAIN_URL}{urls.Url.LOGIN_COURIER_URL}/', data = params )
        return response

    @staticmethod
    def delete_login(login_id):
        params = {'id': login_id}
        with allure.step("Создаем запрос удаления курьера"):
            response_delete = requests.delete(f"{urls.Url.MAIN_URL}{urls.Url.DELETE_COURIER_URL}{login_id}", params=params)
        return response_delete.status_code
