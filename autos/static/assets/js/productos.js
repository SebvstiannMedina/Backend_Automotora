// Lista de productos (arreglo)
const productos = [
    { id: 1, nombre: 'Frenos', precio: 120, img: 'frenos.jpg' },
    { id: 2, nombre: 'Limpiavidrios', precio: 15, img: 'limpiavidrios.jpg' },
    { id: 3, nombre: 'Aceite de Motor', precio: 50, img: 'aceite.jpg' },
    { id: 4, nombre: 'Batería', precio: 100, img: 'bateria.jpg' }
];

// Cargar productos dinámicamente
function cargarProductos() {
    const productosContainer = document.getElementById('productos');
    productos.forEach(producto => {
        const productoHTML = `
            <div class="col-md-3">
                <div class="card mb-4 shadow-sm">
                    <img src="./assets/IMG/${producto.img}" class="card-img-top" alt="${producto.nombre}">
                    <div class="card-body">
                        <h5 class="card-title">${producto.nombre}</h5>
                        <p class="card-text">Precio: $${producto.precio}</p>
                        <button class="btn btn-primary" onclick="agregarAlCarrito(${producto.id})">Añadir al Carrito</button>
                    </div>
                </div>
            </div>
        `;
        productosContainer.innerHTML += productoHTML;
    });
}

// Función para agregar productos al carrito (local storage)
function agregarAlCarrito(id) {
    const producto = productos.find(p => p.id === id);
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push(producto);
    localStorage.setItem('carrito', JSON.stringify(carrito));
    alert(`${producto.nombre} ha sido añadido al carrito`);
}

// Cargar productos al cargar la página
window.onload = () => {
    cargarProductos();
    obtenerValores();  // También cargar los valores financieros
};
