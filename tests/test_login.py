import allure
import requests
import pytest
import data
import generators
from curls import Curls


class TestLogin:
    @allure.title('Тест авторизации существующего пользователя')
    def test_login_user(self):
        payload = {'email': data.UserData.EMAIL,
                   'password': data.UserData.PASSWORD,}
        with allure.step('Авторизация пользователя'):
            responce = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data= payload)
        assert responce.status_code == 200
        assert responce.json()['success'] == True
        assert responce.json()['user'] == {'email': data.UserData.EMAIL,
                                           'name': data.UserData.USER_NAME}

    @allure.title('Тест авторизации с невалидными данными')
    @pytest.mark.parametrize('payload, case_title', 
                             [({'email': generators.generate_email(), 'password': data.UserData.PASSWORD}, 'неверный email'),
                            ({'email': data.UserData.EMAIL, 'password': generators.generate_password()}, 'неверный пароль')
                            ])
    def test_login_invalid_data(self, payload, case_title):
        with allure.step(f'Авторизация с {case_title}'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=payload)
        assert response.status_code == 401
        assert response.json() == data.ResponseData.RESPONSE_INVALID_LOGIN
        