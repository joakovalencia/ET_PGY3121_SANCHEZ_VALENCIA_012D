const $tiempo = document.querySelector('.tiempo');

function digitalClock(){
    let f = new Date()
    dia = f.getDate(),
    mes = f.getMonth(),
    anio = f.getFullYear(),
    diaSemana = f.getDay();

    let timeString = f.toLocaleTimeString();
    $tiempo.innerHTML = timeString;
}
setInterval(() => {
    digitalClock()
},1000);

$(document).ready(function(){

    /* validacion formulario de ingreso de productos */
    $(function(){
        $("#formulario").validate({
            rules:{
                codigo: "required",
                nombre: "required",
                precio: "required",
                stock: "required",
                categoria: "required",
            },
            messages:{
                codigo:{
                    required: 'Ingrese un codigo',
                },
                nombre:{
                    required: 'Ingrese el nombre del producto',
                },
                precio:{
                    required: 'Ingrese el precio',
                },
                stock:{
                    required: 'Ingrese la cantidad de productos',
                },
                imagen:{
                    required: 'Seleccione una imagen',
                },
                categoria:{
                    required: 'Seleccione una categoria',
                },
            }
        });
    });

    $(function(){
        $("#formularioLogin").validate({
            rules:{
                username: "required",
                password: "required",
            },
            messages:{
                username:{
                    required: 'Ingrese su nombre de usuario',
                },
                password:{
                    required: 'Ingrese su contraseña',
                },
            }
        });
    });

    $(function(){
        $("#formUsuario").validate({
            rules:{
                username: "required",
                first_name: "required",
                last_name: "required",
                email: "required",
                password1: "required",
                password2: "required",
            },
            messages:{
                username:{
                    required: 'Ingrese un nombre de usuario',
                },
                first_name:{
                    required: 'Ingrese su nombre',
                },
                last_name:{
                    required: 'Ingrese su apellido',
                },
                email:{
                    required: 'Ingrese un email',
                },
                password1:{
                    required: 'Ingrese una contraseña',
                },
                password2:{
                    required: 'Confirme la contraseña',
                },
            }
        });
    });


    var cambio = false;

    $("#botonfunda").on('click',function(){
        if(cambio){
            $("#imgfunda").css('width', 100)
        } else {
            $("#imgfunda").css('width', 250)
        }
        cambio = !cambio
    });
});

function colorBuscar(obj){
    obj.style.backgroundColor = 'grey';
};

function colorBuscarOut(obj){
    obj.style.backgroundColor = 'white';
};

function colorBotonBuscar(obj){
    obj.style.backgroundColor = 'red';
    obj.style.color = 'black';
};

function colorBotonBuscarOut(obj){
    obj.style.backgroundColor = 'orange';
    obj.style.color = 'white';
};

