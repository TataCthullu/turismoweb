// Evitar entrada fantasma al mover el cursor fuera de los botones
const buttons = document.querySelectorAll('button');
buttons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.cursor = 'pointer';
    });
});
