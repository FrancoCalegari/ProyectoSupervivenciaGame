# ==========================================
# STREAMBOX
# BUILD 2.3.6.0
# CATALOGO + SMART CART
# ==========================================

import customtkinter as ctk
from PIL import Image
import os



class CatalogoStreamBox(ctk.CTkFrame):


    def __init__(
            self,
            parent,
            agregar_callback=None
    ):

        super().__init__(
            parent,
            fg_color="transparent"
        )


        self.agregar_callback = agregar_callback


        self.crear_catalogo()



    # ======================================
    # CREAR CATALOGO
    # ======================================

    def crear_catalogo(self):


        titulo = ctk.CTkLabel(
            self,
            text="🎬 CATÁLOGO",
            font=(
                "Arial",
                32,
                "bold"
            )
        )

        titulo.pack(
            pady=20
        )



        contenido = [

            {
                "nombre":"Ahsoka",
                "poster":"assets/posters/ahsoka_poster.jpeg",
                "fondo":"assets/fondos/ahsoka_fondo.jpeg",
                "precio":"$2500"
            },


            {
                "nombre":"Heart of the Beast",
                "poster":"assets/posters/beast_poster.jpeg",
                "fondo":"assets/fondos/beast_fondo.jpeg",
                "precio":"$3000"
            },


            {
                "nombre":"Record of Ragnarok",
                "poster":"assets/posters/ragnarok_poster.jpeg",
                "fondo":"assets/fondos/ragnarok_fondo.jpeg",
                "precio":"$2800"
            }

        ]



        contenedor = ctk.CTkScrollableFrame(
            self,
            fg_color="transparent"
        )


        contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )



        for pelicula in contenido:

            self.crear_tarjeta(
                contenedor,
                pelicula
            )



    # ======================================
    # TARJETA
    # ======================================

    def crear_tarjeta(
            self,
            parent,
            pelicula
    ):


        tarjeta = ctk.CTkFrame(
            parent,
            fg_color="#151A24",
            corner_radius=15
        )


        tarjeta.pack(
            fill="x",
            pady=15
        )



        # POSTER

        imagen = Image.open(
            pelicula["poster"]
        )


        imagen = imagen.resize(
            (180,250)
        )


        foto = ctk.CTkImage(
            imagen,
            size=(180,250)
        )


        poster = ctk.CTkLabel(
            tarjeta,
            image=foto,
            text=""
        )


        poster.image = foto


        poster.pack(
            side="left",
            padx=20,
            pady=20
        )



        # INFORMACION

        info = ctk.CTkFrame(
            tarjeta,
            fg_color="transparent"
        )


        info.pack(
            side="left",
            fill="both",
            expand=True,
            padx=20
        )



        nombre = ctk.CTkLabel(
            info,
            text=pelicula["nombre"],
            font=(
                "Arial",
                24,
                "bold"
            )
        )


        nombre.pack(
            pady=10
        )



        precio = ctk.CTkLabel(
            info,
            text="Precio: "+pelicula["precio"],
            font=(
                "Arial",
                16
            )
        )


        precio.pack()



        boton = ctk.CTkButton(
            info,
            text="🛒 Agregar al carrito",
            command=lambda:
                self.agregar(
                    pelicula
                )
        )


        boton.pack(
            pady=15
        )



    # ======================================
    # AGREGAR
    # ======================================

    def agregar(
            self,
            pelicula
    ):


        if self.agregar_callback:

            self.agregar_callback(
                pelicula
            )