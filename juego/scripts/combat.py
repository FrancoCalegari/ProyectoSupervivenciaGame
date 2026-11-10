# 🧟 SupervivenciaGame
# Sistema de Combate
# Versión: v0.1.1

import random


class Combate:

    def __init__(self, jugador):

        self.jugador = jugador
        self.enemigo_actual = None

        self.estado = "Exploración"

        self.golpes_realizados = 0
        self.enemigos_derrotados = 0


    def iniciar_combate(self, enemigo):

        self.enemigo_actual = enemigo
        self.estado = "Combate"

        print("=" * 45)
        print("⚔️ COMBATE INICIADO")
        print("=" * 45)

        print(
            f"🧍 {self.jugador.nombre}"
            f" vs "
            f"🧟 {enemigo.nombre}"
        )


    def atacar_con_arma(self, arma):

        if self.enemigo_actual is None:

            print(
                "❌ No hay enemigo"
            )

            return


        if self.estado != "Combate":

            print(
                "❌ No estás en combate"
            )

            return


        daño = arma.daño


        # Probabilidad de golpe crítico
        critico = random.randint(1, 100)


        if critico <= 15:

            daño *= 2

            print(
                "💥 GOLPE CRÍTICO"
            )


        print(
            f"🔫 {arma.nombre}"
            f" causa {daño} de daño"
        )


        self.enemigo_actual.recibir_daño(
            daño
        )


        self.golpes_realizados += 1


        self.comprobar_estado()



    def ataque_cuerpo_a_cuerpo(self):

        if self.enemigo_actual is None:

            print(
                "❌ No hay enemigo"
            )

            return


        daño = 15


        print(
            f"👊 Ataque cuerpo a cuerpo:"
            f" {daño} daño"
        )


        self.enemigo_actual.recibir_daño(
            daño
        )


        self.comprobar_estado()



    def recibir_ataque(self):

        if self.enemigo_actual:

            daño = self.enemigo_actual.daño


            print(
                f"🧟 Zombie ataca:"
                f" {daño} daño"
            )


            self.jugador.recibir_daño(
                daño
            )


            if self.jugador.vida <= 0:

                self.derrota()



    def comprobar_estado(self):

        if self.enemigo_actual.vida <= 0:

            self.victoria()



    def victoria(self):

        print("=" * 45)
        print("🏆 ENEMIGO DERROTADO")
        print("=" * 45)


        self.estado = "Victoria"

        self.enemigos_derrotados += 1


        experiencia = 25


        self.jugador.ganar_experiencia(
            experiencia
        )


        print(
            f"⭐ +{experiencia} experiencia"
        )



    def derrota(self):

        print("=" * 45)
        print("☠️ JUGADOR DERROTADO")
        print("=" * 45)


        self.estado = "Derrota"



    def mostrar_estadisticas(self):

        print("=" * 45)
        print("📊 ESTADÍSTICAS DE COMBATE")
        print("=" * 45)

        print(
            "Golpes realizados:",
            self.golpes_realizados
        )

        print(
            "Enemigos derrotados:",
            self.enemigos_derrotados
        )

        print(
            "Estado:",
            self.estado
        )