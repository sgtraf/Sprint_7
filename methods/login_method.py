import requests
import data

class LoginMethods:

    @staticmethod
    def login_in_system(login, password):
        params = {'login': login, 'password': password}
        responce = requests.post(f'{data.Url.MAIN_URL}{data.Url.LOGIN_COURIER_URL}/', data = params )
        courier_id = responce.json()
        return courier_id["id"]

print(LoginMethods.login_in_system('ninjarer', '1234'))
