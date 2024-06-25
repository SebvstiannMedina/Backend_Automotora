function validar() {
    var user = $("#user").val();
    var email = $("#email").val();
    var pass1 = $("#pass1").val();
    var pass2 = $("#pass2").val();
    var sexoMasculino = $("#sexo-masculino").prop("checked");
    var sexoFemenino = $("#sexo-femenino").prop("checked");
    var terminos = $("#terminos").prop("checked");

    // Validación de campos vacíos
    if (user == "" || email == "" || pass1 == "" || pass2 == "" || (!sexoMasculino && !sexoFemenino) || !terminos) {
        alert("Por favor, completa todos los campos y acepta los términos y condiciones.");
        return false;
    }

    // Validación de dirección de correo electrónico
    var emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Por favor, introduce una dirección de correo electrónico válida.");
        return false;
    }

    // Validación de contraseña
    if (pass1 !== pass2) {
        alert("Las contraseñas no coinciden.");
        return false;
    }

    // Si todas las validaciones son exitosas, el formulario se enviará
    return true;
}

