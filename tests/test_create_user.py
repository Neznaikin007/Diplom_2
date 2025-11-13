import allure
import requests
import pytest
import data
from curls import Curls

class TestCreateUser:
    @allure.title('Тест создания уникального пользователя')
    def test_create_user(self, generate_data_and_delete_user):
        payload = generate_data_and_delete_user
        with allure.step('Создание пользователя'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data = payload)
        assert response.status_code == 200
        assert response.json()['user'] == {'email': payload['email'], 'name': payload['name']}
    
    @allure.title('Тест создания пользователя, который уже зарегистрирован')
    def test_create_existing_user(self):
        payload = {'email': data.UserData.EMAIL,
                   'password': data.UserData.PASSWORD,
                   'name': data.UserData.USER_NAME}
        with allure.step('Создание уже зарегистированного пользователя'):
            responce = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data= payload)
        assert responce.status_code == 403
        assert responce.json() == data.ResponseData.RESPONSE_CREATE_EXISTING_USER

    @allure.title('Тест создания пользователя без одного из обязательных полей')
    @pytest.mark.parametrize('missing_field, payload', data.TestData.test_data)
    def test_create_user_without_field(self, missing_field, payload):
        with allure.step(f'Создание пользователя без {missing_field}'):
            response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_REGISTRATION}', data= payload)
        assert response.status_code == 403
        assert response.json() == data.ResponseData.RESPONSE_CREATE_USER_MISSING_FIELD
                