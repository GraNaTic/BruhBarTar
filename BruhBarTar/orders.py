from bottle import route, template, post, request
from datetime import datetime
import json
import re

@route('/add_product', method='post')
def add_product():
    with open('orders.json') as file:
        data = json.load(file)
    with open('orders_history.json') as file:
        history = json.load(file)
    select_product = request.forms.getunicode("product_name")
    return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=select_product, error=None, history=history)

@route('/buy', method='post')
def buy():
    error=None
    with open('orders.json') as file:
        data = json.load(file)
    with open('orders_history.json') as file:
        history = json.load(file)
    select_product=request.forms.getunicode("product_name")
    email=request.forms.getunicode("EMAIL")
    name=request.forms.getunicode("NAME")
    address=request.forms.getunicode("ADDRESS")
    phone=request.forms.getunicode("PHONE")
    if not validate_email(email):
        error = "Неверно введена почта!"
    elif email.strip() == '' or name.strip() == '' or name.strip() == '' or address.strip() == '':
        error = "Заполните все поля!"
    elif not validate_name(name):
        error = "Некорректно введено имя!"
    elif not validate_address(address):
        error = "Некорректно введен адрес!"
    elif not validate_phone(phone):
        error = "Некорректно введен телефон! Пример: +79234562347"
    if error is None:
        new_record = {
            "product_name": select_product,
            "name": name,
            "address": address,
            "phone": phone,
            "email": email,
            "date": str(datetime.today().date())
        }
        
        history.append(new_record)
        
        # Открываем файл на запись и записываем обновленные данные
        with open('orders_history.json', 'w') as f:
            json.dump(history, f)
        return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=None, error=error, history=history)
    elif error is not None:
        return template('orders', title='Вклад капибар в культуру человека', year=datetime.now().year, data=data, select_product=select_product, error=error, history=history)

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
    # Проверка наличия ключевых элементов в адресе
    required_elements = ["ул.", "г.", "д.", "кв."]
    for element in required_elements:
        if element not in address:
            return False  # Отсутствует обязательный элемент в адресе

    return True  # Адрес валиден

