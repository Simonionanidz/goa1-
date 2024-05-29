
// Sample product data
const productsData = [
    { name: "Смартфон", price: 500, image: "phone.jpgn.jpeg" },
    // Add more products as needed
];
// Function to display products on the page
function displayProducts() {
    const productsContainer = document.getElementById("products");

    productsData.forEach(product => {
        const productElement = document.createElement("article");
        productElement.classList.add("product");

        const imageElement = document.createElement("img");
        imageElement.src = product.image;
        imageElement.alt = product.name;

        const nameElement = document.createElement("h2");
        nameElement.textContent = product.name;

        const priceElement = document.createElement("p");
        priceElement.classList.add("price");
        priceElement.textContent = `Цена: $${product.price}`;

        const addButton = document.createElement("button");
        addButton.textContent = "Добавить в корзину";
        addButton.addEventListener("click", () => addToCart(product));

        productElement.appendChild(imageElement);
        productElement.appendChild(nameElement);
        productElement.appendChild(priceElement);
        productElement.appendChild(addButton);

        productsContainer.appendChild(productElement);
    });
}

// Function to add product to cart
function addToCart(product) {
    // Implement your cart logic here
    console.log(`Product added to cart: ${product.name}`);
}

// Display products when the page loads
window.addEventListener("load", displayProducts);