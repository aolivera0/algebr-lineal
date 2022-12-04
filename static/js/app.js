document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("form-suma").addEventListener('submit', validarFormularioSuma);
    document.getElementById("form-escalar").addEventListener('submit', validarFormularioEsca);
    document.getElementById("form-mult").addEventListener('submit', validarFormularioMult);
    document.getElementById("form-traza").addEventListener('submit', validarFormularioTraza);
    document.getElementById("form-transpuesta").addEventListener('submit', validarFormularioTranspuesta);
    document.getElementById("form-inversa").addEventListener('submit', validarFormularioInversa);
    document.getElementById("form-determinante").addEventListener('submit', validarDeterminante);
    document.getElementById("form-norma").addEventListener('submit', validarFormularioNorma);
    document.getElementById("form-direccion").addEventListener('submit', validarFormularioDireccion);
    document.getElementById("form-unitario").addEventListener('submit', validarFormularioUnitario);
    document.getElementById("form-productoPunto").addEventListener('submit', validarFormularioProductoPunto);
    document.getElementById("form-gram").addEventListener('submit', validarFormularioGram);
    document.getElementById("form-valores").addEventListener('submit', validarFormularioValores);
    document.getElementById("form-vectores").addEventListener('submit', validarFormularioVectores);
    document.getElementById("form-gauss").addEventListener('submit', validarFormularioGauss);
});

function validarFormularioSuma(evento) {
    evento.preventDefault();
    var filas = document.querySelector('#filas-suma');
    var columnas = document.querySelector('#columnas-suma');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioEsca(evento) {
    evento.preventDefault();
    var filas = document.querySelector('#filas-escalar');
    var columnas = document.querySelector('#columnas-escalar');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioMult(evento) {
    evento.preventDefault();
    var filasA = document.querySelector('#filasA-mult');
    var filasB = document.querySelector("#filasB-mult")
    var columnasA = document.querySelector('#columnasA-mult');
    var columnasB = document.querySelector('#columnasB-mult');

    if (filasA.selectedIndex == 0 || filasB.selectedIndex == 0 || columnasA.selectedIndex == 0 || columnasB.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else if(columnasA.selectedIndex != filasB.selectedIndex) {
        alert("Recuerde que para multiplicar matrices el número de columnas de la columna A debe ser igual al número de filas de la columna B");
    } else {
        this.submit();
    }
}

function validarFormularioTraza(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-traza');
    var columnas = document.querySelector('#columnas-traza');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioTranspuesta(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-transpuesta');
    var columnas = document.querySelector('#columnas-transpuesta');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioInversa(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-inversa');
    var columnas = document.querySelector('#columnas-inversa');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else if(filas.selectedIndex != columnas.selectedIndex) {
        alert("Recuerde que la matriz debe ser cuadrada");
    } else {
        this.submit();
    }
}

function validarDeterminante(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-determinante');
    var columnas = document.querySelector('#columnas-determinante');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else if(filas.selectedIndex != columnas.selectedIndex) {
        alert("Recuerde que la matriz debe ser cuadrada");
    } else {
        this.submit();
    }
}

function validarFormularioNorma(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-norma');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioDireccion(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-direccion');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioUnitario(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-unitario');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioProductoPunto(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-productoPunto');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioGram(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-gram');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioValores(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-valores');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioVectores(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-vectores');
    
    if (filas.selectedIndex == 0){
        alert("Seleccione una opción válida");
    } else {
        this.submit();
    }
}

function validarFormularioGauss(evento){
    evento.preventDefault();
    var filas = document.querySelector('#filas-gauss');
    var columnas = document.querySelector('#columnas-gauss');

    if (filas.selectedIndex == 0 || columnas.selectedIndex == 0){
        alert('Seleccione una opción válida')
    } else {
        this.submit();
    }
}