# ==========================================
# STREAMBOX
# BUILD 2.3.5.0
# CONTROL CENTER + SMART CART
# ==========================================

import customtkinter as ctk


from config import (
    NOMBRE_APP,
    BUILD,
    ANCHO_VENTANA,
    ALTO_VENTANA,
    COLOR_PRINCIPAL,
    COLOR_CIAN,
    COLOR_TEXTO
)


from fondo import colocar_fondo
from menu import MenuLateral
from catalogo import CatalogoStreamBox
from smart_cart import SmartCart



# ==========================================
# INTERFAZ PRINCIPAL
# ==========================================

class InterfazStreamBox(ctk.CTk):


    def __init__(self):

        super().__init__()

        self.configurar_ventana()



    # ======================================
    # CONFIGURACION
    # ======================================

    def configurar_ventana(self):

        self.title(
            f"{NOMBRE_APP} - BUILD {BUILD}"
        )


        self.geometry(
            f"{ANCHO_VENTANA}x{ALTO_VENTANA}"
        )


        self.configure(
            fg_color=COLOR_PRINCIPAL
        )



    # ======================================
    # LABEL PARA ANIMACION
    # ======================================

    def crear_label(
            self,
            texto,
            tamaño,
            color
    ):

        return ctk.CTkLabel(
            self,
            text=texto,
            font=(
                "Arial",
                tamaño,
                "bold"
            ),
            text_color=color
        )



    # ======================================
    # CARGAR CENTRO CONTROL
    # ======================================

    def cargar_centro_control(self):

        self.crear_interfaz()



    # ======================================
    # CREAR INTERFAZ
    # ======================================

    def crear_interfaz(self):


        colocar_fondo(
            self,
            ANCHO_VENTANA,
            ALTO_VENTANA
        )



        self.contenedor = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )


        self.contenedor.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )



        # PANEL PRINCIPAL

        self.panel = ctk.CTkFrame(
            self.contenedor,
            fg_color="#101824"
        )


        self.panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=20
        )



        # MENU

        self.menu = MenuLateral(
            self.contenedor,
            self.mostrar_inicio,
            self.mostrar_catalogo,
            self.mostrar_carrito
        )


        self.menu.pack(
            side="left",
            fill="y"
        )



        self.mostrar_inicio()



    # ======================================
    # LIMPIAR PANEL
    # ======================================

    def limpiar_panel(self):


        for widget in self.panel.winfo_children():

            widget.destroy()



    # ======================================
    # INICIO
    # ======================================

    def mostrar_inicio(self):


        self.limpiar_panel()


        titulo = ctk.CTkLabel(
            self.panel,
            text="STREAMBOX",
            font=(
                "Arial",
                40,
                "bold"
            ),
            text_color=COLOR_CIAN
        )


        titulo.pack(
            pady=80
        )



        texto = ctk.CTkLabel(
            self.panel,
            text="Centro de Control Futurista",
            font=(
                "Arial",
                18
            ),
            text_color=COLOR_TEXTO
        )


        texto.pack()



    # ======================================
    # CATALOGO
    # ======================================

    def mostrar_catalogo(self):


        self.limpiar_panel()


        catalogo = CatalogoStreamBox(
            self.panel
        )


        catalogo.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # SMART CART
    # ======================================

    def mostrar_carrito(self):


        self.limpiar_panel()


        carrito = SmartCart(
            self.panel
        )


        carrito.pack(
            fill="both",
            expand=True
        )