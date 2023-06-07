% rebase('layout.tpl', title=title, year=year, error = error, cont = cont)

<div id="description">
    <form id = "reviewForm" method="post" onsubmit="sendReview(event)">
            <h1>Напишите свой отзыв здесь</h1>
            <p><input id="login" type="text" size="50" name="LOGIN" placeholder="Ваш логин"></p>            
            <p><textarea id="review" rows="2" cols="50" name="REVIEW" placeholder="Оставьте свой отзыв здесь"></textarea></p>
            <p>Дата обращения к сайту</p>
            <p><input id="date" type="date" size="50" name="DATE"></p>
            <p><span id="err" style="color:red;">{{error}}</span></p>
            <p><input class="btn btn-default" type="submit" value="Отправить"></p>
    </form>
</div>
<script src="/static/scripts/Grisha.js"></script>
<div id="content">{{!cont}}</div>