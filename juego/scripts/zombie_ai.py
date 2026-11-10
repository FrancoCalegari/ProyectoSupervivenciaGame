# 🧟 SupervivenciaGame
# Sistema de IA Avanzada de Zombies
# Versión: v0.1.1


import math
import random


class ZombieIA:

    def __init__(self, zombie):

        self.zombie = zombie

        # Estado actual de la inteligencia artificial
        self.estado = "Patrullando"

        # Distancias de comportamiento
        self.distancia_deteccion = 15
        self.distancia_ataque = 2

        # Objetivo del zombie
        self.objetivo = None

        # Sistema de sonido
        self.ruido_detectado = False
        self.posicion_ruido = None



    def detectar_jugador(self, jugador):

        distancia = self.calcular_distancia(
            self.zombie.posicion,
            jugador.posicion
        )


        if distancia <= self.distancia_deteccion:

            self.objetivo = jugador
            self.estado = "Alerta"

            print(
                f"👁️ {self.zombie.nombre} detectó a "
                f"{jugador.nombre}"
            )

        else:

            print(
                "🧟 Zombie no detectó al jugador"
            )



    def actualizar(self):

        print(
            f"🤖 Estado IA: {self.estado}"
        )


        if self.estado == "Patrullando":

            self.patrullar()


        elif self.estado == "Alerta":

            self.perseguir()


        elif self.estado == "Persiguiendo":

            self.perseguir()


        elif self.estado == "Atacando":

            self.atacar()


        elif self.estado == "Investigando":

            self.investigar_ruido()



    def patrullar(self):

        movimiento = random.choice(
            [
                "izquierda",
                "derecha",
                "adelante",
                "atrás"
            ]
        )


        print(
            f"🚶 Zombie patrullando hacia {movimiento}"
        )



    def perseguir(self):

        if self.objetivo is None:

            self.estado = "Patrullando"

            return


        distancia = self.calcular_distancia(
            self.zombie.posicion,
            self.objetivo.posicion
        )


        print(
            f"🏃 Zombie persigue objetivo "
            f"distancia: {round(distancia,2)}"
        )


        if distancia <= self.distancia_ataque:

            self.estado = "Atacando"

            print(
                "⚠️ Zombie está cerca del jugador"
            )

        else:

            self.zombie.mover_hacia_objetivo()



    def atacar(self):

        if self.objetivo:

            print(
                "💥 IA ejecuta ataque"
            )


            self.zombie.atacar()


            self.estado = "Persiguiendo"



    def escuchar_ruido(
        self,
        posicion
    ):

        self.ruido_detectado = True
        self.posicion_ruido = posicion

        self.estado = "Investigando"


        print(
            "👂 Zombie escuchó un ruido"
        )



    def investigar_ruido(self):

        if self.ruido_detectado:

            print(
                "🔎 Zombie investigando sonido"
            )


            self.zombie.posicion = (
                self.posicion_ruido.copy()
            )


            self.ruido_detectado = False

            self.estado = "Patrullando"



    def recibir_daño(self):

        print(
            "😡 Zombie recibió daño y aumenta agresividad"
        )


        if self.objetivo:

            self.estado = "Persiguiendo"



    def calcular_distancia(
        self,
        posicion1,
        posicion2
    ):

        x1 = posicion1["x"]
        y1 = posicion1["y"]

        x2 = posicion2["x"]
        y2 = posicion2["y"]


        distancia = math.sqrt(
            (x2 - x1) ** 2 +
            (y2 - y1) ** 2
        )


        return distancia