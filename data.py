import generators


# Данные поьзователя дял авторизации
class UserData:
    EMAIL = 'mihail@mail.ru'
    PASSWORD = '1234567'
    USER_NAME = 'Mihail'

# Данные пользователя для изменения профиля
class UserDataForChange:
    EMAIL = 'mihail_change@mail.ru'
    PASSWORD = '1234567'
    USER_NAME = 'Mihail'

# Данные ингредиентов для заказов
class Ingredients:
    INVALID_HASH = ['61c0c5a71d1f82001bdaaa6', '16c0c5a71d1f82001bdaaa61']


#Ожидаемые ответы от API
class ResponseData:
    RESPONSE_CREATE_EXISTING_USER = {'success': False,
                                     'message': 'User already exists'}
    RESPONSE_CREATE_USER_MISSING_FIELD = {'success': False,
                                          'message': 'Email, password and name are required fields'}
    RESPONSE_INVALID_LOGIN = {'success': False,
                              'message': 'email or password are incorrect'}
    RESPONSE_INVALID_CREATE_ORDER = {'success': False,
                                    'message': 'Ingredient ids must be provided'}   

# Тестовые данныне для полей
class TestData:
    test_data = [
    ('email', {'password': generators.generate_password(), 'name': generators.generate_name()}),
    ('password', {'email': generators.generate_email(), 'name': generators.generate_name()}),
    ('name', {'email': generators.generate_email(), 'password': generators.generate_password()})
    ]
