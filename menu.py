# ==========================================
# STREAMBOX
# BUILD 2.3.5.0
# MENU LATERAL CON MODULOS
# ==========================================

import customtkinter as ctk


class MenuLateral(ctk.CTkFrame):


    def __init__(
            self,
            parent,
            mostrar_inicio=None,
            mostrar_catalogo=None,
            mostrar_carrito=None
    ):

        super().__init__(
            parent,
            width=230,
            corner_radius=0,
            fg_color="#0B1320"
        )


        self.mostrar_inicio = mostrar_inicio
        self.mostrar_catalogo = mostrar_catalogo
        self.mostrar_carrito = mostrar_carrito


        self.crear_menu()



    # ======================================
    # CREAR MENU
    # ======================================

    def crear_menu(self):


        titulo = ctk.CTkLabel(
            self,
            text="STREAMBOX",
            font=(
                "Arial",
                24,
                "bold"
            ),
            text_color="#48CAE4"
        )


        titulo.pack(
            pady=(30,20)
        )



        self.crear_boton(
            "🏠 Inicio",
            self.inicio
        )


        self.crear_boton(
            "🎬 Catálogo",
            self.catalogo
        )


        self.crear_boton(
            "🛒 Smart Cart",
            self.carrito
        )


        self.crear_boton(
            "💳 Pagos"
        )


        self.crear_boton(
            "📚 Biblioteca"
        )


        self.crear_boton(
            "🤖 AURA"
        )


        self.crear_boton(
            "⚙ Configuración"
        )



    # ======================================
    # BOTON
    # ======================================

    def crear_boton(
            self,
            texto,
            comando=None
    ):


        boton = ctk.CTkButton(

            self,

            text=texto,

            height=40,

            corner_radius=10,

            fg_color="#101D30",

            hover_color="#1D4E89",

            command=comando

        )


        boton.pack(

            padx=20,

            pady=8,

            fill="x"

        )



    # ======================================
    # ACCIONES
    # ======================================

    def inicio(self):

        if self.mostrar_inicio:

            self.mostrar_inicio()



    def catalogo(self):

        if self.mostrar_catalogo:

            self.mostrar_catalogo()



    def carrito(self):

        if self.mostrar_carrito:

            self.mostrar_carrito()