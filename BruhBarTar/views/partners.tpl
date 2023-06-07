% rebase('layout.tpl', title='Партнеры', year=year, error=error)

<h1 id="company">Наши партнеры</h1>
  
  <div >
      <div id="partners" class="partner-grid">
      % for email, company_data in data.items():
        <div class="partner-card">
            <img class="partner-logo" src="{{ company_data['logo'] }}" alt="Логотип">
            <h2>{{ company_data['name'] }}</h2>
            <p>{{ company_data['description'] }}</p>
            <p>Год начала партнерства: {{ company_data['partnershipDate'] }}</p>
        </div>
      % end
    </div>
</div>
<div id="cmp">
<div class="join">
  <h3> Стать партнером </h3>
    <form action="/companies" method="post">
        <p>Заполните поля для сотрудничества</p>
        <p><input type="text" size="50" name="NAME" placeholder="Название компании, начиная с заглавной буквы"></p>
        <p><input type="text" size="50" name="ADDRESS" placeholder="Официальный электронный адрес"></p>
        <p><textarea rows="2" cols="50" name="DES" placeholder="Вставьте описание компании для сайта, начиная с заглавной буквы, не более 300 символов, но не менее 30"></textarea></p> 
        <p><textarea rows="2" cols="50" name="IMG" placeholder="Вставьте ссылку на логотип в формате https://......"></textarea></p>
        <p><span style="color:red;">{{error}}</span></p>
        <p><input class="btn btn-default" type="submit" value="Отправить"></p>
    </form>
</div>
</div>