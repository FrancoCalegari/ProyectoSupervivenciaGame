/* =====================================
   PROJECT INFINITY
   BUILD 1.0.0.0
   JAVASCRIPT
===================================== */



// Mensaje inicial al cargar la plataforma

window.onload = function(){


    console.log(
        "🌌 PROJECT INFINITY iniciado correctamente"
    );


};





// ===============================
// BUSCADOR INICIAL
// ===============================


const searchInput = document.querySelector(
    ".search-box input"
);


const searchButton = document.querySelector(
    ".search-box button"
);



if(searchButton){


    searchButton.addEventListener(
        "click",
        function(){


            let texto = searchInput.value;


            if(texto.trim() === ""){


                alert(
                    "Escribí un juego para buscar."
                );


            }

            else{


                alert(
                    "Buscando: " + texto
                );


            }


        }
    );


}







// ===============================
// BOTONES DE JUEGOS
// ===============================


const gameButtons = document.querySelectorAll(
    ".game-card button"
);



gameButtons.forEach(
    
    function(button){


        button.addEventListener(
            "click",
            function(){


                alert(
                    "Esta función estará disponible en futuras versiones de Project Infinity."
                );


            }
        );


    }

);







// ===============================
// FUTURA BASE DE PERFIL
// ===============================


let usuario = {


    nombre:
    "Usuario",


    nivel:
    1,


    logros:
    0,


    insignias:
    0


};



console.log(usuario);







// ===============================
// FUTURA BASE DE AVATAR
// BUILD 3.0.0.0
// ===============================


let avatar = {


    tipo:
    "Inicial",


    nivel:
    1,


    titulo:
    "Jugador Nuevo"


};



console.log(avatar);







// ===============================
// FUTURA BASE DE CONFIGURACION
// ===============================


let configuracion = {


    sonido:
    true,


    efectos:
    true,


    modo:
    "oscuro"


};



console.log(configuracion);