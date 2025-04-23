import allure
import pytest
from methods.login_method import LoginMethods
from methods.generators import GenerateBody


@pytest.fixture
def generate_login_data():
    test_body = GenerateBody.generate_body()
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

@pytest.fixture
def generate_without_login_data():
    test_body = GenerateBody.generate_body()
    test_body['login'] = ''
    return test_body

@pytest.fixture
def generate_without_password_data():
    test_body = GenerateBody.generate_body()
    test_body['login'] = ''
    return test_body

@pytest.fixture
def generate_two_courier_with_same_login_data():
    test_body = GenerateBody.generate_body()
    with allure.step("Создаем курьера"):
        LoginMethods.register_new_courier_and_return_login_password(test_body)
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

#Фикстуры второго задания.
#Создается логин со случайными параметрами, залогиниваемся получаем id и код ответа, потом удаляем логин из базы.
@pytest.fixture
def get_login_id():
    test_body = GenerateBody.generate_body()
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

#Создается логин со случайными параметрами, залогиниваемся без пароля, код ответа, потом удаляем логин из базы.
@pytest.fixture
def get_login_without_password():
    test_body = GenerateBody.generate_body()
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

#Создается логин со случайными параметрами, залогиниваемся с неправильным паролем, потом удаляем логин из базы.
@pytest.fixture
def get_login_with_incorrect_password():
    test_body = GenerateBody.generate_body()
    yield test_body
    with allure.step("Удаляем курьера"):
        LoginMethods.delete_login(LoginMethods.login_in_system(test_body['login'], test_body['password']).json()["id"])

#Вход под несуществующим пользователем.
@pytest.fixture
def get_login_with_unreal_data():
    test_body = GenerateBody.generate_body()
    return test_body
