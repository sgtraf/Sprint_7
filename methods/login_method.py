import requests
import data


class LoginMethods:

    @staticmethod
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    def register_new_courier_and_return_login_password(body):

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=body)

        #  добавляем в список логин и пароль курьера
        login_pass.append(body['login'])
        login_pass.append(body['password'])
        login_pass.append(body['firstName'])
        login_pass.append(response)

        # возвращаем список
        return login_pass


    @staticmethod
    def login_in_system(login, password):
        params = {'login': login, 'password': password}
        response = requests.post(f'{data.Url.MAIN_URL}{data.Url.LOGIN_COURIER_URL}/', data = params )
        courier_id = response.json()
        return response #[courier_id["id"], response.status_code]


    @staticmethod
    def delete_login(login_id):
        params = {'id': login_id}
        response_delete = requests.delete(f"{data.Url.MAIN_URL}{data.Url.DELETE_COURIER_URL}{login_id}", params=params)
        return response_delete.status_code


#login_pass = LoginMethods.register_new_courier_and_return_login_password()
##print(login_pass[3].status_code)
#print(LoginMethods.login_in_system(login_pass[0], login_pass[1]))
#print(LoginMethods.delete_login(LoginMethods.login_in_system(login_pass[0], login_pass[1])))
