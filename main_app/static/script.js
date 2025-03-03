document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".buy-btn").forEach(button => {
        button.addEventListener("click", (event) => {
            let productId = event.target.dataset.product;
            fetch(`/add-to-cart/${productId}/`, { method: "POST", headers: { "X-CSRFToken": getCookie("csrftoken") } })
            .then(response => response.json())
            .then(data => alert("Produkt dodany do koszyka!"));
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        document.cookie.split(';').forEach(cookie => {
            let trimmed = cookie.trim();
            if (trimmed.startsWith(name + '=')) {
                cookieValue = decodeURIComponent(trimmed.substring(name.length + 1));
            }
        });
    }
    return cookieValue;
}