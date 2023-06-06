% rebase('layout.tpl')

<h1>Оформленные заказы</h1>
    <div id="product" class="orders-grid">
      % for product in data:
        <div class="orders-card">
          <form action="/add_product" method="post">
            <img class="orders-logo" src="{{ product['image_url'] }}" alt="Товар">
            <h2>{{ product['product_name'] }}</h2>
            <input type="hidden" name="product_name" value="{{ product['product_name'] }}">
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
        <p>{{"Купить "+select_product}}</p>
        <p><input type="text" size="50" name="NAME" placeholder="Имя получателя"></p>
        <p><input type="text" size="50" name="EMAIL" placeholder="Электронный адрес"></p>
        <p><input type="text" size="50" name="ADDRESS" placeholder="Адрес доставки"></p>
        <p><input type="text" size="50" name="PHONE" placeholder="Контактный телефон"></p>
        <p><span style="color:red;">{{error}}</span></p>
        <p><input class="btn btn-default" type="submit" value="Отправить"></p>
    </form>
</div>

% end