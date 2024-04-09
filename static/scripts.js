// Evitar entrada fantasma al mover el cursor fuera de los botones
const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.cursor = 'pointer';
    });
});

document.addEventListener("DOMContentLoaded", function() {
    // Obtener todos los contenedores de botones de destino
    var contenedoresBotones = document.querySelectorAll('.boton-destino');
    
    // Agregar un controlador de eventos clic a cada contenedor de botón
    contenedoresBotones.forEach(function(contenedor) {
        contenedor.addEventListener('click', function(event) {
            // Obtener el botón dentro del contenedor
            var boton = contenedor.querySelector('button');
            
            // Acción deseada al hacer clic en el botón, por ejemplo, redireccionar al usuario a la página de información del destino
            // Aquí puedes obtener el texto del botón haciendo referencia al contenido del botón (boton.textContent)
            // Luego puedes usar este texto para realizar alguna acción específica, como redirigir al usuario a una página particular
            console.log("Botón de destino clicado:", boton.textContent);
            
            // Evitar la propagación del evento clic para evitar que se ejecute en el contenedor externo
            event.stopPropagation();
        });
    });
});

