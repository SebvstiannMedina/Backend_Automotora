let vehiculos = [
    { marca: 'Toyota', modelo: 'Corolla', año: 2020, precio: 20000 },
    { marca: 'Honda', modelo: 'Civic', año: 2019, precio: 18000 },
    { marca: 'Ford', modelo: 'Mustang', año: 2021, precio: 35000 }
];

let carrito = [];
const vehiculosPorPagina = 5;
let paginaActual = 1;

function mostrarVehiculos(filtrados = vehiculos) {
    const lista = document.getElementById('vehiculos-lista');
    lista.innerHTML = '';
    const inicio = (paginaActual - 1) * vehiculosPorPagina;
    const vehiculosPagina = filtrados.slice(inicio, inicio + vehiculosPorPagina);

    vehiculosPagina.forEach((vehiculo, index) => {
        const vehiculoDiv = document.createElement('div');
        vehiculoDiv.className = 'vehiculo card mb-3';

        vehiculoDiv.innerHTML = `
            <div class="card-body">
                <h5 class="card-title">${vehiculo.marca} ${vehiculo.modelo}</h5>
                <p class="card-text">Año: ${vehiculo.año}</p>
                <p class="card-text">Precio: $${vehiculo.precio}</p>
                <button class="btn btn-info" onclick="verDetalles(${inicio + index})">Detalles</button>
                <button class="btn btn-success" onclick="agregarAlCarrito(${inicio + index})">Agregar al carrito</button>
                <button class="btn btn-danger" onclick="eliminarVehiculo(${inicio + index})">Eliminar</button>
            </div>
        `;

        lista.appendChild(vehiculoDiv);
    });

    mostrarPaginacion(filtrados.length);
}

function mostrarPaginacion(totalVehiculos) {
    const paginacion = document.getElementById('paginacion');
    paginacion.innerHTML = '';
    const totalPaginas = Math.ceil(totalVehiculos / vehiculosPorPagina);

    for (let i = 1; i <= totalPaginas; i++) {
        const li = document.createElement('li');
        li.className = `page-item ${i === paginaActual ? 'active' : ''}`;
        li.innerHTML = `<button class="page-link" onclick="cambiarPagina(${i})">${i}</button>`;
        paginacion.appendChild(li);
    }
}

function cambiarPagina(nuevaPagina) {
    paginaActual = nuevaPagina;
    mostrarVehiculos();
}

document.getElementById('form-agregar-vehiculo').addEventListener('submit', function(event) {
    event.preventDefault();
    const nuevaMarca = document.getElementById('marca').value;
    const nuevoModelo = document.getElementById('modelo').value;
    const nuevoAño = parseInt(document.getElementById('año').value);
    const nuevoPrecio = parseFloat(document.getElementById('precio').value);

    vehiculos.push({ marca: nuevaMarca, modelo: nuevoModelo, año: nuevoAño, precio: nuevoPrecio });
    mostrarVehiculos();
    document.getElementById('form-agregar-vehiculo').reset();
});

function eliminarVehiculo(index) {
    vehiculos.splice(index, 1);
    mostrarVehiculos();
}

document.getElementById('buscar').addEventListener('input', function() {
    const termino = this.value.toLowerCase();
    const vehiculosFiltrados = vehiculos.filter(vehiculo => vehiculo.marca.toLowerCase().includes(termino));
    mostrarVehiculos(vehiculosFiltrados);
});

function verDetalles(index) {
    const vehiculo = vehiculos[index];
    const detallesCuerpo = document.getElementById('detallesCuerpo');
    detallesCuerpo.innerHTML = `
        <h5>${vehiculo.marca} ${vehiculo.modelo}</h5>
        <p>Año: ${vehiculo.año}</p>
        <p>Precio: $${vehiculo.precio}</p>
    `;
    const detallesModal = new bootstrap.Modal(document.getElementById('detallesModal'));
    detallesModal.show();
}

function agregarAlCarrito(index) {
    carrito.push(vehiculos[index]);
    alert('Vehículo agregado al carrito');
}

function verCarrito() {
    if (carrito.length === 0) {
        alert('El carrito está vacío');
    } else {
        let resumenCarrito = 'Vehículos en el carrito:\n';
        carrito.forEach((vehiculo, index) => {
            resumenCarrito += `${index + 1}. ${vehiculo.marca} ${vehiculo.modelo} - $${vehiculo.precio}\n`;
        });
        alert(resumenCarrito);
    }
}

window.onload = mostrarVehiculos;
