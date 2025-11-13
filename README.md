## Дипломный проект. Задание 2: API-тесты
<hr>

## Студент: Роман Попов

## <h>Когорта: #28+29_qa_FS</h>
<hr>

## <h>Project: Stellar Burger API</h>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest --alluredir=allure_results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла          | Содержание файла               |
|-------------------------|--------------------------------|
| Tests dir               | Директория с тестами           |
| test_create_user.py     | Тесты на создание пользователя |
| test_login.py           | Тесты на авторизацию           |
| test_create_order.py    | Тесты на создание заказа       |
| conftest.py             | Фикстуры                       |
| data.py                 | Файл с body запросов           |
| curls.py                | Файсл с URL                    |
| generators.py           | Генератор данных               |
| requirements.txt        | Файл с зависимостями           |
| allure_results.dir      | Папка с отчетами Allure        |



