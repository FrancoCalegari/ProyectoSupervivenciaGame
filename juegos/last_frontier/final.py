# ==========================================
# STREAMBOX
# BUILD 2.5.2.4
# UI + CHECKOUT + TICKET CONNECTOR
# ==========================================

import customtkinter as ctk


from config import (
    NOMBRE_APP,
    BUILD,
    ANCHO_VENTANA,
    ALTO_VENTANA,
    COLOR_PRINCIPAL,
    COLOR_CIAN
)


from fondo import colocar_fondo
from menu import MenuLateral
from catalogo import CatalogoStreamBox
from smart_cart import SmartCart
from detalle import DetalleContenido
from pago import PagoStreamBox
from ticket import TicketStreamBox



class InterfazStreamBox(ctk.CTk):


    def __init__(self):

        super().__init__()


        self.carrito = []


        self.configurar_ventana()



    # ======================================
    # VENTANA
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
    # LABEL PARA ANIMACIONES
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
    # CARGAR SISTEMA
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
            expand=True
        )



        self.panel = ctk.CTkFrame(
            self.contenedor,
            fg_color="#101824"
        )


        self.panel.pack(
            side="right",
            fill="both",
            expand=True
        )



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



    # ======================================
    # CATALOGO
    # ======================================

    def mostrar_catalogo(self):


        self.limpiar_panel()


        catalogo = CatalogoStreamBox(
            self.panel,
            self.agregar_carrito,
            self.mostrar_detalle
        )


        catalogo.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # DETALLE
    # ======================================

    def mostrar_detalle(
            self,
            contenido
    ):


        self.limpiar_panel()


        detalle = DetalleContenido(
            self.panel,
            contenido,
            self.mostrar_catalogo,
            self.agregar_carrito
        )


        detalle.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # CARRITO
    # ======================================

    def mostrar_carrito(self):


        self.limpiar_panel()


        carrito = SmartCart(
            self.panel,
            self.carrito,
            self.mostrar_pago
        )


        carrito.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # CHECKOUT
    # ======================================

    def mostrar_pago(
            self,
            contenido
    ):


        self.limpiar_panel()


        pago = PagoStreamBox(
            self.panel,
            contenido,
            self.mostrar_ticket,
            self.mostrar_carrito
        )


        pago.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # TICKET
    # ======================================

    def mostrar_ticket(
            self,
            contenido,
            metodo
    ):


        self.limpiar_panel()


        ticket = TicketStreamBox(
            self.panel,
            contenido,
            metodo,
            self.mostrar_inicio
        )


        ticket.pack(
            fill="both",
            expand=True
        )



    # ======================================
    # AGREGAR AL CARRITO
    # ======================================

    def agregar_carrito(
            self,
            contenido
    ):


        self.carrito.append(
            contenido
        )


        print(
            "CARRITO:",
            self.carrito
        )