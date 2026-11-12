# 🧟 SupervivenciaGame
# Sistema Jugador + Inventario
# FASE 2.2
# Versión v0.2.2


import sys
import os


ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

if ruta_scripts not in sys.path:
    sys.path.insert(0, ruta_scripts)


from inventory import Inventario



class Jugador:


    def __init__(
        self,
        nombre
    ):

        self.nombre = nombre

        # Estado

        self.vida = 100
        self.energia = 100
        self.hambre = 100
        self.sed = 100


        # Progreso

        self.nivel = 1
        self.experiencia = 0


        # Posición

        self.posicion = {

            "x": 0,
            "y": 0

        }


        self.zona_actual = "Inicio"


        # Inventario real

        self.inventario = Inventario(
            peso_maximo=30
        )



    # -------------------------
    # Movimiento
    # -------------------------

    def mover(
        self,
        direccion
    ):

        if direccion == "norte":

            self.posicion["y"] += 1


        elif direccion == "sur":

            self.posicion["y"] -= 1


        elif direccion == "este":

            self.posicion["x"] += 1


        elif direccion == "oeste":

            self.posicion["x"] -= 1



    # -------------------------
    # Cambiar zona
    # -------------------------

    def cambiar_zona(
        self,
        zona
    ):

        self.zona_actual = zona



    # -------------------------
    # Recibir objetos
    # -------------------------

    def recibir_item(
        self,
        item
    ):


        resultado = self.inventario.agregar_item(
            item
        )


        if resultado:

            print(
                f"🎒 {self.nombre} obtuvo {item.nombre} x{item.cantidad}"
            )


        return resultado



    # -------------------------
    # Comer
    # -------------------------

    def comer(
        self,
        nombre="Comida enlatada"
    ):


        objeto = self.inventario.buscar(
            nombre
        )


        if objeto:


            if self.inventario.quitar_item(
                nombre,
                1
            ):


                self.hambre += 25


                if self.hambre > 100:

                    self.hambre = 100


                print(
                    "🍞 Hambre recuperada"
                )


        else:

            print(
                "❌ No tienes comida"
            )



    # -------------------------
    # Beber
    # -------------------------

    def beber(
        self,
        nombre="Agua"
    ):


        objeto = self.inventario.buscar(
            nombre
        )


        if objeto:


            if self.inventario.quitar_item(
                nombre,
                1
            ):


                self.sed += 30


                if self.sed > 100:

                    self.sed = 100


                print(
                    "💧 Sed recuperada"
                )


        else:

            print(
                "❌ No tienes agua"
            )



    # -------------------------
    # Daño
    # -------------------------

    def recibir_danio(
        self,
        cantidad
    ):


        self.vida -= cantidad


        if self.vida < 0:

            self.vida = 0


        print(
            f"💥 Daño recibido: {cantidad}"
        )



    # -------------------------
    # Curar
    # -------------------------

    def curar(
        self,
        cantidad
    ):


        self.vida += cantidad


        if self.vida > 100:

            self.vida = 100



    # -------------------------
    # Experiencia
    # -------------------------

    def ganar_experiencia(
        self,
        cantidad
    ):


        self.experiencia += cantidad


        print(
            f"⭐ Experiencia +{cantidad}"
        )


        if self.experiencia >= 100:

            self.nivel += 1

            self.experiencia = 0


            print(
                f"⬆️ Nivel aumentado: {self.nivel}"
            )



    # -------------------------
    # Mostrar estado
    # -------------------------

    def mostrar_estado(
        self
    ):


        print("=" * 60)

        print(
            f"🧍 Jugador: {self.nombre}"
        )

        print(
            f"❤️ Vida: {self.vida}"
        )

        print(
            f"⚡ Energía: {self.energia}"
        )

        print(
            f"🍖 Hambre: {self.hambre}"
        )

        print(
            f"💧 Sed: {self.sed}"
        )

        print(
            f"⭐ Nivel: {self.nivel}"
        )

        print(
            f"📍 Zona: {self.zona_actual}"
        )

        print()

        self.inventario.mostrar()