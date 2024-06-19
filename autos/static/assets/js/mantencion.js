
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("registroMantenimientoForm");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evitar que el formulario se envíe automáticamente

        // Validar los campos del formulario
        const nombre = document.getElementById("nombre").value.trim();
        const apellidos = document.getElementById("apellidos").value.trim();
        const correo = document.getElementById("correo").value.trim();
        const fechaMantenimiento = document.getElementById("fechaMantenimiento").value.trim();
        const modelo = document.getElementById("modelo").value.trim();
        const año = document.getElementById("año").value.trim();
        const tipoVehiculo = document.getElementById("tipoVehiculo").value.trim();

        if (nombre === "" || apellidos === "" || correo === "" || fechaMantenimiento === "" || modelo === "" || año === "" || tipoVehiculo === "") {
            alert("Por favor completa todos los campos.");
            return;
        }

        // Validar formato de correo electrónico
        const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!correoRegex.test(correo)) {
            alert("Por favor ingresa un correo electrónico válido.");
            return;
        }

        // Validar año como número entero positivo
        const añoRegex = /^[0-9]+$/;
        if (!añoRegex.test(año) || parseInt(año) < 0) {
            alert("Por favor ingresa un año válido.");
            return;
        }

        // Si todos los campos son válidos, se puede enviar el formulario
        alert("¡Registro de mantenimiento enviado con éxito!");
        form.reset(); // Limpiar el formulario después de enviarlo
    });
});
