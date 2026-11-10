# 🧟 SupervivenciaGame
# Sistema de Zombies
# Versión: v0.1.1


class Zombie:

    def __init__(self, tipo="Comun"):

        # Información básica
        self.tipo = tipo
        self.nombre = f"Zombie {tipo}"

        # Estadísticas
        self.vida = 100
        self.daño = 10
        self.velocidad = 2

        # Estado
        self.estado = "Activo"

        # Posición
        self.posicion = {
            "x": 10,
            "y": 10
        }

        # Objetivo actual
        self.objetivo = None


    def mostrar_estado(self):

        print("=" * 40)
        print("🧟 ESTADO DEL ZOMBIE")
        print("=" * 40)

        print(f"Tipo: {self.tipo}")
        print(f"Vida: {self.vida}")
        print(f"Daño: {self.daño}")
        print(f"Velocidad: {self.velocidad}")

        print("\n📍 Posición:")
        print(self.posicion)

        print("\nEstado:")
        print(self.estado)


    def detectar_jugador(self, jugador):

        self.objetivo = jugador

        print(
            f"👁️ {self.nombre} detectó a "
            f"{jugador.nombre}"
        )


    def perseguir(self):

        if self.objetivo:

            print(
                f"🧟 {self.nombre} está persiguiendo "
                f"a {self.objetivo.nombre}"
            )

            self.mover_hacia_objetivo()

        else:

            print(
                "❌ No hay objetivo detectado"
            )


    def mover_hacia_objetivo(self):

        if self.objetivo:

            jugador_x = self.objetivo.posicion["x"]
            jugador_y = self.objetivo.posicion["y"]

            if self.posicion["x"] < jugador_x:
                self.posicion["x"] += 1

            elif self.posicion["x"] > jugador_x:
                self.posicion["x"] -= 1


            if self.posicion["y"] < jugador_y:
                self.posicion["y"] += 1

            elif self.posicion["y"] > jugador_y:
                self.posicion["y"] -= 1


            print(
                "🚶 Zombie se acercó al jugador"
            )


    def atacar(self):

        if self.objetivo:

            print(
                f"💥 {self.nombre} atacó"
            )

            self.objetivo.recibir_daño(
                self.daño
            )

        else:

            print(
                "No hay jugador para atacar"
            )


    def recibir_daño(self, daño):

        self.vida -= daño

        print(
            f"⚔️ Zombie recibió {daño} de daño"
        )


        if self.vida <= 0:

            self.morir()


    def morir(self):

        self.vida = 0
        self.estado = "Eliminado"

        print(
            f"☠️ {self.nombre} fue eliminado"
        )


    def cambiar_tipo(self, nuevo_tipo):

        self.tipo = nuevo_tipo
        self.nombre = f"Zombie {nuevo_tipo}"


        if nuevo_tipo == "Rapido":

            self.velocidad = 5
            self.daño = 15


        elif nuevo_tipo == "Tanque":

            self.vida = 300
            self.daño = 25


        elif nuevo_tipo == "Mutante":

            self.vida = 500
            self.daño = 40


        print(
            f"🧬 Zombie cambiado a {nuevo_tipo}"
        )