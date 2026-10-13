// =================================
// PROJECT INFINITY
// SCRIPT WEB 1.1.0
// =================================


function mostrarMensaje(){

    alert(
        "🚀 Bienvenido a PROJECT INFINITY\n\n" +
        "Tu plataforma de videojuegos está iniciando..."
    );

}



function verJuego(nombreJuego){


    if(nombreJuego === "SupervivenciaGame"){

        alert(
            "🧟 SupervivenciaGame\n\n" +
            "Estado: En desarrollo\n" +
            "Género: Supervivencia apocalíptica\n" +
            "Plataforma: Web"
        );

    }


    else if(nombreJuego === "Zona.Cero"){

        alert(
            "⚔ Zona.Cero\n\n" +
            "Estado: Proyecto en desarrollo\n" +
            "Género: Supervivencia mundo abierto"
        );

    }


    else{

        alert(
            "🚀 Próximamente nuevos proyectos."
        );

    }

}



window.addEventListener("load", function(){

    console.log(
        "PROJECT INFINITY iniciado correctamente"
    );

});
