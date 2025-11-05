import requests
import generators
import data
import pytest
from curls import Curls

@pytest.fixture()
def generate_data_and_delete_user():
    payload = {'email': generators.generate_email(),
               'password': generators.generate_password(),
               'name': generators.generate_name()}
    yield payload
    payload_login = {'email': payload['email'],
                     'password': payload['password']}
    response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=payload_login)
    requests.delete(f'{Curls.MAIN_URL}{Curls.URL_DELETE_USER}', headers={'Authorization': response.json()['accessToken']})


@pytest.fixture(scope='session')
def login_user():
    payload = {'email': data.UserData.EMAIL,
               'password': data.UserData.PASSWORD}
    response = requests.post(f'{Curls.MAIN_URL}{Curls.URL_LOGIN}', data=payload)
    return response.json()


@pytest.fixture(scope='session')
def get_ingredients():
    response = requests.get(f'{Curls.MAIN_URL}{Curls.URL_INGREDIENTS}')
    list_ingredients = []
    for i in range(len(response.json()['data'])):
        list_ingredients.append(response.json()['data'][i]['_id'])
    return list_ingredients
