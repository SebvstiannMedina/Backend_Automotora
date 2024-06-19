function guardarAlmacenamientoLocal(llave, valor_a_guardar) {
    localStorage.setItem(llave, JSON.stringify(valor_a_guardar))
}
function obtenerAlmacenamientoLocal(llave) {
    const datos = JSON.parse(localStorage.getItem(llave))
    return datos
}

let productos = obtenerAlmacenamientoLocal('productos') || [];
let contenedor = document.getElementById('contenedor')
window.addEventListener('load', ()=>{
    for (let i = 0; i < productos.length; i++){
        contenedor.innerHTML +=`<div><img src="${productos[i].urlImagen}" alt="producto 1"><div class="informacion"><p>${productos[i].nombre}</p><p class="precio">$${productos[i].valor}</p><button>Comprar</button></div></div>` 
    }
})


const header = document.querySelector("#header");
const body = document.querySelector("body");
window.addEventListener("scroll", function(){
    if(contenedor.getBoundingClientRect().top<10){
        header.classList.add("scroll")
    }
    else{
        header.classList.remove("scroll")
    }
})

// Función para agregar un producto al carrito
function agregarAlCarrito(producto) {
    let carrito = obtenerAlmacenamientoLocal('carrito') || [];
    carrito.push(producto);
    guardarAlmacenamientoLocal('carrito', carrito);
    // Redireccionar a la página de carrito
    window.location.href = 'carrito.html';
}

// Evento de clic para el botón "Comprar" de cada producto
document.addEventListener('click', function(event) {
    if (event.target.classList.contains('comprar-btn')) {
        // Obtener los datos del producto
        const productoIndex = event.target.dataset.index;
        const producto = productos[productoIndex];
        // Agregar el producto seleccionado al carrito
        agregarAlCarrito(producto);
    }
});
