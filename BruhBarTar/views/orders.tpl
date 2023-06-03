% rebase('layout.tpl')

<h1>Оформленные заказы</h1>
    <div id="product" class="orders-grid">
      % for product in data:
        <div class="orders-card">
          <form action="/add_product" method="post">
            <img class="orders-logo" src="{{ product['image_url'] }}" alt="Товар">
            <h2>{{ product['product_name'] }}</h2>
            <p name="product_name" >{{ product['product_name'] }}</p>
            <p>{{ str(product['price'])+' $' }}</p>
            <button  class="btn" type="submit">Заказать</button>
          </form>
        </div>
      % end
    </div>
% if select_product is not None:
  <div class="join">
  <h3>Сделать заказ</h3>
    <form action="/buy" method="post">
        <p>Заполните поля для оформления заказа</p>
        <p><input type="text" size="50" name="NAME" placeholder="Название компании, начиная с заглавной буквы"></p>
        <p><input type="text" size="50" name="ADDRESS" placeholder="Официальный электронный адрес"></p>
        <p><textarea rows="2" cols="50" name="DES" placeholder="Вставьте описание компании для сайта, начиная с заглавной буквы, не более 300 символов, но не менее 30"></textarea></p> 
        <p><textarea rows="2" cols="50" name="IMG" placeholder="Вставьте ссылку на логотип в формате https://......"></textarea></p>
        <p><span style="color:red;">{{error}}</span></p>
        <p><input class="btn btn-default" type="submit" value="Отправить"></p>
    </form>
</div>

% end