import allure
from methods.login_method import LoginMethods

@allure.title('Test Successful login creation')
@allure.description('Тут создаем логин и проверяем ответ API')
class TestCreateLogin:
    def test_create_login(self,generate_login_data):
        responce = generate_login_data
        assert responce.status_code == 201 and responce.json()['ok'] == True

