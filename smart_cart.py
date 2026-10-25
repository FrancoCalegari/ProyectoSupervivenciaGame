# ==========================================
# STREAMBOX
# BUILD 2.3.6.0
# SMART CART
# ==========================================

import customtkinter as ctk



class SmartCart(ctk.CTkFrame):


    def __init__(
            self,
            parent,
            carrito=None
    ):

        super().__init__(
            parent,
            fg_color="transparent"
        )


        self.carrito = carrito if carrito else []


        self.crear_interfaz()



    # ======================================
    # INTERFAZ
    # ======================================

    def crear_interfaz(self):


        titulo = ctk.CTkLabel(
            self,
            text="🛒 SMART CART",
            font=(
                "Arial",
                32,
                "bold"
            )
        )


        titulo.pack(
            pady=20
        )



        if len(self.carrito)==0:


            vacio = ctk.CTkLabel(
                self,
                text="El carrito está vacío",
                font=(
                    "Arial",
                    18
                )
            )


            vacio.pack(
                pady=40
            )


        else:


            for item in self.carrito:


                producto = ctk.CTkLabel(
                    self,
                    text=
                    f"🎬 {item['nombre']}  -  {item['precio']}",
                    font=(
                        "Arial",
                        18
                    )
                )


                producto.pack(
                    pady=10
                )