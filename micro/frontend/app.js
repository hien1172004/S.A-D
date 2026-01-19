const CUSTOMER_API = "http://localhost:8001/api/customers";
const BOOK_API = "http://localhost:8002/api/books";
const CART_API = "http://localhost:8003/api/cart";

/* ===== REGISTER ===== */
function register() {
  fetch(`${CUSTOMER_API}/register/`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    })
  })
  .then(r => r.json())
  .then(data => {
    if(data.error){
      alert(data.error);
    } else {
      alert("Register success");
      window.location = "login.html";
    }
  });
}

/* ===== LOGIN ===== */
function login() {
  fetch(`${CUSTOMER_API}/login/`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    })
  })
  .then(r => r.json())
  .then(data => {
    if(data.id){
      localStorage.setItem("customer_id", data.id);
      window.location = "books.html";
    } else {
      document.getElementById("msg").innerText = "Login failed";
    }
  });
}

/* ===== LOAD BOOKS ===== */
if (document.getElementById("books")) {
  fetch("http://localhost:8002/api/books/")
    .then(r => r.json())
    .then(data => {
      const list = document.getElementById("books");
      list.innerHTML = "";

      data.forEach(b => {
        list.innerHTML += `
          <li>
            <b>${b.title}</b> - $${b.price}
            <input type="number" id="qty-${b.id}" value="1" min="1" style="width:50px">
            <button onclick="addToCart(${b.id})">Add to Cart</button>
          </li>
        `;
      });
    });
}


/* ===== ADD TO CART ===== */
function addToCart(bookId){
  const qty = document.getElementById("qty-" + bookId).value;

  fetch(`${CART_API}/add/`, {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      customer_id: localStorage.getItem("customer_id"),
      book_id: bookId,
      quantity: qty
    })
  })
  .then(r => r.json())
  .then(_ => alert("Added to cart"));
}

/* ===== VIEW CART ===== */
if(document.getElementById("cart")){
  fetch(`${CART_API}/${localStorage.getItem("customer_id")}/`)
    .then(r => r.json())
    .then(data => {
      data.forEach(i => {
        document.getElementById("cart").innerHTML += `
          <li>${i.title} x ${i.quantity} = $${i.price * i.quantity}</li>
        `;
      });
    });
}
