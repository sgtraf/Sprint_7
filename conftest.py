import pytest
from methods.login_method import LoginMethods
from methods.generators import GenerateBody

@pytest.fixture
def generate_login_data():
    test_body = GenerateBody.generate_body()
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = login_body[3]
    yield body
    LoginMethods.delete_login(LoginMethods.login_in_system(login_body[0], login_body[1]).json()["id"])

@pytest.fixture
def generate_two_courier_with_same_login():
    login_body = LoginMethods.register_two_courier_with_same_login()
    body = login_body[4]
    yield body
    LoginMethods.delete_login(LoginMethods.login_in_system(login_body[0], login_body[1]).json()["id"])

@pytest.fixture
def generate_without_login_data():
    test_body = GenerateBody.generate_body()
    test_body['login'] = ''
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = login_body[3]
    return body

@pytest.fixture
def generate_without_password_data():
    test_body = GenerateBody.generate_body()
    test_body['login'] = ''
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = login_body[3]
    return body

@pytest.fixture
def generate_two_courier_with_same_login_data():
    test_body = GenerateBody.generate_body()
    LoginMethods.register_new_courier_and_return_login_password(test_body)
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = login_body[3]
    yield body
    LoginMethods.delete_login(LoginMethods.login_in_system(login_body[0], login_body[1]).json()["id"])

#Фикстуры второго задания.
#Создается логин со случайными параметрами, залогиниваемся получаем id и код ответа, потом удаляем логин из базы.
@pytest.fixture
def get_login_id():
    test_body = GenerateBody.generate_body()
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = LoginMethods.login_in_system(login_body[0], login_body[1])
    yield body
    LoginMethods.delete_login(body.json()["id"])

#Создается логин со случайными параметрами, залогиниваемся получаем id и код ответа, потом удаляем логин из базы.
@pytest.fixture
def get_login_withot_password():
    test_body = GenerateBody.generate_body()
    login_body = LoginMethods.register_new_courier_and_return_login_password(test_body)
    body = LoginMethods.login_in_system(login_body[0], login_body[1])
    print(body.json()["id"])
    body_answer_withot_pass = LoginMethods.login_in_system(login_body[0], '')
    yield body_answer_withot_pass
    LoginMethods.delete_login(body.json()["id"])