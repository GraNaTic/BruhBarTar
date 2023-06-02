from bottle import post, request,template
import re
from datetime import datetime
import json
import os

def email_check(str):
    email_pattern = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+' # Регулярное выражение для проверки почты на корректность формата
    if re.match(email_pattern,str) == None:
        return False
    else:
        return True

def validate_description(description):
    if description.strip() == '':
        return False
    if len(description) < 30:
        return False
    if len(description) > 300:
        return False
    if not description[0].isupper():
        return False
    if description.isdigit():
        return False
    if not re.match(r'^[A-Za-zА-Яа-я0-9.,!?\'\"\- ]*$', description):
        return False
    return True

def validate_company_name(name):
    if len(name) < 2:
        return False
    if len(name) > 40:
        return False
    if not name[0].isupper():
        return False
    if re.match(r'^[A-Za-zА-Яа-я0-9 ]*$', name) is None:
        return False
    if name.isdigit():
        return False
    return True

def validate_logo_url(url):
    if re.match(r'^(https://)[^s/$.?].[^\s]*$', url) is None:
        return False
    if url.strip() == '':
        return False
    return True

@post('/companies', method='post')
def my_form():
    email = request.forms.get('ADDRESS')
    name = request.forms.getunicode('NAME')
    descr = request.forms.getunicode('DES')
    url = request.forms.getunicode('IMG')
    error = None
    c = 0
    with open('partners.json','r', encoding='utf-8') as json_file:
            data = json.load(json_file)
    if any(item.get(email) and item[email]["name"] == name for item in data.values()):
        error = "Компания с такой почтой и названием уже существует!"
    if not email_check(email):
        error = "Некорректный формат почты!"
    elif email.strip() == '' or name.strip() == '' or descr.strip() == '' or url.strip() == '':
        error = "Заполните все поля!"
    elif not validate_description(descr):
        error = "Некорректно заполнено описание компании!"
    elif not validate_company_name(name):
        error = "Некорректно введено название компании!"
    elif not validate_logo_url(url):
        error = "Некорректная ссылка на логотип!"
    if email in data:
        companies = data[email]
        for company in companies:
            if company['name'] == company_name:
                error = "Данная компания уже является нашим партнером"
                break
        else:
            c=1
            

    if error:
        year=datetime.now().year
        return template('partners.tpl', error=error, year=year, data = data)
    else:
        if (c==1):
            new_partner = {
                "name": name,
                "logo": url,
                "description": descr,
                "partnershipDate": datetime.now().year
            }
            companies.append(new_partner)
        else:
            new_partner = {
                email: {
                    "name": name,
                    "logo": url,
                    "description": descr,
                    "partnershipDate": datetime.now().year
                }
            }
        data.update(new_partner)
        with open('partners.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        return f"Спасибо, {name}! Ваша компания добавлена на сайт, мы свяжемся с вами касательно партнерства по вашей почте {email}."

