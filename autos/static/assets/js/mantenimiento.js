function enviarSolicitud() {
    const fecha = document.getElementById('fecha').value;
    const tipoServicio = document.getElementById('tipoServicio').value;

    // Aquí puedes realizar la solicitud a la API de calendario (este es un ejemplo ficticio)
    // Reemplaza este código con la integración real con la API de calendario que estés utilizando
    // Aquí simplemente mostramos un mensaje en lugar de hacer la solicitud real
    const mensaje = `Fecha: ${fecha}, Tipo de Servicio: ${tipoServicio}`;
    document.getElementById('mensaje').innerText = mensaje;
}
