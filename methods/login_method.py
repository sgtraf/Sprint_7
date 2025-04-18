import requests
import data
import random
import string

class LoginMethods:

    @staticmethod
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass


    @staticmethod
    def login_in_system(login, password):
        params = {'login': login, 'password': password}
        responce = requests.post(f'{data.Url.MAIN_URL}{data.Url.LOGIN_COURIER_URL}/', data = params )
        courier_id = responce.json()
        return courier_id["id"]


    @staticmethod
    def delete_login(login_id):
        params = {'id': login_id}
        response_delete = requests.delete(f"{data.Url.MAIN_URL}{data.Url.DELETE_COURIER_URL}{login_id}", params=params)
        return response_delete.status_code




print(LoginMethods.login_in_system('ninjarer', '1234'))
print(LoginMethods.delete_login(LoginMethods.login_in_system('ninjarer', '1234')))
