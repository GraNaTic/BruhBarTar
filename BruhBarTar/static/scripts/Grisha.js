function sendReview(event) {
    event.preventDefault();
    let data = new FormData(document.getElementById("reviewForm"));
    fetch("/reviews", {
        method: 'POST',
        cache: 'no-cache',
        body: data
    })
    .then(response => response.json())
    .then(data => {
    if (data.message === "") {
        var html = data.newReview + document.getElementById("content").innerHTML;
        document.getElementById("content").innerHTML = html;
    }
    else {
        document.getElementById("err").innerHTML = data.message;
    }
});
}