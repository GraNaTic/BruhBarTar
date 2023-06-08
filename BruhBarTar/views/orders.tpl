% rebase('layout.tpl')

<h1>ВЫбрать товар:</h1>
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
    <h1>Оформленные заказы</h1>
    <div class="result">
    <table>
        <thead>
            <tr>
                 <th>Товар</th>
                 <th>Имя</th>
                 <th>Адрес</th>
                 <th>Телефон</th>
                 <th>Электронная почта</th>
                 <th>Дата</th>
            </tr>
        </thead>
        <tbody>
            % for i in history:
                <tr>
                     <td>{{ i['product_name'] }}</td>
                     <td>{{ i['name'] }}</td>
                     <td>{{ i['address'] }}</td>
                     <td>{{ i['phone'] }}</td>
                     <td>{{ i['email'] }}</td>
                     <td>{{ i['date'] }}</td>
                </tr>
            % end
        </tbody>
    </table>
    </div>
% if select_product is not None:
  <div class="join">
  <h3>Сделать заказ</h3>
    <form action="/buy" method="post">
        <p>{{"Товар: "+select_product}}</p>
        <input type="hidden" name="product_name" value="{{ select_product }}">
        <p><input type="text" size="50" name="NAME" placeholder="Имя получателя"></p>
        <p><input type="text" size="50" name="EMAIL" placeholder="Электронный адрес"></p>
        <p><input type="text" size="50" name="ADDRESS" placeholder="Адрес доставки"></p>
        <p><input type="text" size="50" name="PHONE" placeholder="Контактный телефон"></p>
        % if error is not None:
        <p><span style="color:red;">{{error}}</span></p>
        % end
        <p><input class="btn btn-default" type="submit" value="Отправить"></p>
    </form>
</div>

% end