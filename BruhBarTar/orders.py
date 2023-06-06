from bottle import route, template, post, request
from datetime import datetime
import json

@route('/add_product', method='post')
def add_product():
    with open('orders.json') as file:
        data = json.load(file)
    select_product = request.forms.getunicode("product_name")
    return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=select_product, error=None)

@route('/buy', method='post')
def buy():
    return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=None, error=None)

def validate_email(email):
    # Шаблон регулярного выражения для проверки формата адреса электронной почты
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Проверяем, соответствует ли адрес электронной почты заданному шаблону
    if re.match(email_pattern, email):
        return True  # Адрес электронной почты валиден

    return False  # Адрес электронной почты невалиден

def validate_name(name):
    # Шаблон регулярного выражения для проверки имени
    name_pattern = r"^[А-Яа-яЁё\s]+$"
    # Проверяем, соответствует ли имя заданному шаблону
    if re.match(name_pattern, name):
        return True  # Имя валидно
    return False  # Имя невалидно


def validate_phone(phone):
    # Шаблон регулярного выражения для проверки номера телефона
    phone_pattern = r"^\+7\d{10}$"  # Проверяем, что номер начинается с "+7" и содержит ровно 10 цифр

    # Проверяем, соответствует ли номер телефона заданному шаблону
    if re.match(phone_pattern, phone):
        return True  # Номер телефона валиден

    return False  # Номер телефона невалиден


def validate_address(address):
    # Проверяем, содержит ли адрес хотя бы одно непустое значение
    if not address.strip():
        return False  # Адрес пустой
    # Проверяем формат адреса

    # В данном примере мы просто проверяем наличие ключевых элементов в адресе
    required_elements = ["ул.", "г.", "д."]
    for element in required_elements:
        if element not in address:
            return False  # Отсутствует обязательный элемент в адресе

    return True  # Адрес валиден

