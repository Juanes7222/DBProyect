// Empty JS for your own code to be here

function ajustarPieDePagina() {
    const contenido = document.querySelector('main');
    const pieDePagina = document.querySelector('footer');

    const contenidoAltura = contenido.clientHeight;
    const ventanaAltura = window.innerHeight;

    if (contenidoAltura < ventanaAltura) {
        const espacioEnBlanco = ventanaAltura - contenidoAltura;
        pieDePagina.style.marginTop = espacioEnBlanco + 'px';
    } else {
        pieDePagina.style.marginTop = '0';
    }
}

// Llama a la función al cargar la página y cada vez que se agrega contenido dinámico
ajustarPieDePagina();


