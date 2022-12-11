
$(document).ready(function() {
    // cuando presiono el boton btnSubmit 
    // hace una llamada a la funcion onclick
    $("#guardar_HC").click(function(){

        var campo_nombre = $("#validationName").val();
        var campo_apellido =$("#validationLastName").val();
        var campo_CI =$ ("#validationCI").val();
        var campo_edad =$ ("#validationAge").val();
        var campo_sexo =$ ("#validationSex").val();
        var campo_telef =$ ("#validationPhone").val();
        var campo_direccion =$ ("#validationDirection").val();

        if ((campo_nombre.length ==0) || (campo_apellido.length ==0) || (campo_CI.length ==0) || (campo_edad.length ==0)
        || (campo_sexo.length ==0) || (campo_telef.length ==0)|| (campo_direccion.length ==0)) {
            alert("El campo nombre no puede estar vacío.");
        }
        else if(){}
        // esto me permite redirigir mi sitio hacia otra pagina, 
        // solo si los campos estan validados
        else{            
            // me redirecciona a otra pagina
            window.location.href = 'Principal.html';                     
        }

    });
    });