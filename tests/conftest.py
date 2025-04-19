import pytest
from methods.login_method import LoginMethods


@pytest.fixture
def generate_login_data():
    login_body = LoginMethods.register_new_courier_and_return_login_password()
    body = login_body[3]
    yield body
    LoginMethods.delete_login(LoginMethods.login_in_system(login_body[0], login_body[1]))