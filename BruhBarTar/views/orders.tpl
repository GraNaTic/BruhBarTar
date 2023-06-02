% rebase('layout.tpl')

<h1>Оформленные заказы</h1>
    <div id="partners" class="orders-grid">
      % for product in data:
        <div class="orders-card">
            <img class="orders-logo" src="{{ product['image_url'] }}" alt="Товар">
            <h2>{{ product['product_name'] }}</h2>
            <p>{{ product['price'] }}</p>
            <button class="btn">Заказать</button>
        </div>
      % end
    </div>