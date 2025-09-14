const products = [
    { id: 1, name: "ლეპტოპი", price: 1200 },
    { id: 2, name: "ტელეფონი", price: 800 },
    { id: 3, name: "ყურსასმენი", price: 150 },
];

const productList = document.getElementById("productList");
const cart = document.getElementById("cart");


for (let i = 0; i < products.length; i++) {
    const product = products[i];
    const div = document.createElement("div");
    div.className = "product";
    div.innerHTML = `
        <h3>${product.name}</h3>
        <p>ფასი: ${product.price}₾</p>
        <button onclick="addToCart(${product.id})">კალათში დამატება</button>
      `;
    productList.appendChild(div);
}


function addToCart(id) {
    const item = products.find(p => p.id === id);
    const div = document.createElement("div");
    div.textContent = `${item.name} - ${item.price}₾`;
    cart.appendChild(div);
}