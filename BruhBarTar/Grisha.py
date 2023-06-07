from bottle import post, request, template
import re
from datetime import date, datetime
import json
import os.path

@post('/reviews', method='post')
def my_form():
    login = request.forms.get('LOGIN')
    reviewText = request.forms.getunicode('REVIEW')
    dateOfVisit = request.forms.get('DATE')
    data = {}
    response_data = {'newReview':"", 'message':""}
    if not os.path.isfile('C:\\Users\\Grisha\\source\\repos\\BruhBarTar\\BruhBarTar\\reviews.json'): #Проверка на наличие файла
        data[login] = [[reviewText, dateOfVisit]]
    else:
        with open('reviews.json') as json_file:
            data=json.load(json_file)				        
        if checkLogin(login):
            if checkDate(dateOfVisit):
                if login in data:
                    data[login].append([reviewText, dateOfVisit])
                else:
                    data[login]=[[reviewText, dateOfVisit]]
            else:
                response_data['message'] = "Выбранная вами дата неверна"
                return json.dumps(response_data)
        else:
            response_data['message'] = "Введённый логин невалиден"
            return json.dumps(response_data)
    with open('reviews.json', 'w') as outfile:
        json.dump(data, outfile)
    ret=""
    ret+="<div class = \"cardReview\"><h3>"+login+"</h3><p>"+dateOfVisit+"</p><p class=\"reviewText\">"+reviewText+"</p></div>"
    response_data['newReview'] = ret
    return json.dumps(response_data)



def checkLogin(login):
    if len(login)<4 or len(login)>10:
        return False
    if login.isdigit():
        return False
    return True

def checkDate(dateOfVisit):
    date_format = "%Y-%m-%d"
    regex = r'^\d{4}-\d{2}-\d{2}$'
    match = re.match(regex, dateOfVisit)
    if not match:
        return False
    else:
        dateOfVisit = datetime.strptime(dateOfVisit, date_format).date()
        if dateOfVisit<datetime.strptime("2023-05-01", date_format).date():
            return False
        if dateOfVisit>date.today():
            return False
        return True