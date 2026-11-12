# 🧟 SupervivenciaGame
# Sistema del Jugador
# FASE 2 - Mundo Jugable
# Versión v0.2.0


class Jugador:


    def __init__(
        self,
        nombre
    ):

        # Información básica

        self.nombre = nombre


        # Estadísticas

        self.vida = 100

        self.vida_maxima = 100

        self.energia = 100

        self.energia_maxima = 100

        self.hambre = 100

        self.sed = 100


        # Experiencia

        self.nivel = 1

        self.experiencia = 0



        # Posición en el mundo

        self.posicion = {

            "x": 0,

            "y": 0

        }



        # Zona actual

        self.zona_actual = "Inicio"



        # Estado

        self.estado = "Normal"



    # -------------------------
    # Movimiento
    # -------------------------


    def mover(
        self,
        direccion
    ):


        if self.energia <= 0:

            print(
                "⚡ No tienes energía para moverte"
            )

            return False



        if direccion == "norte":

            self.posicion["y"] += 1



        elif direccion == "sur":

            self.posicion["y"] -= 1



        elif direccion == "este":

            self.posicion["x"] += 1



        elif direccion == "oeste":

            self.posicion["x"] -= 1



        else:

            print(
                "❌ Dirección incorrecta"
            )

            return False



        self.energia -= 5


        print(
            f"🚶 {self.nombre} se movió hacia {direccion}"
        )


        print(
            f"📍 Posición: {self.posicion}"
        )


        return True



    # -------------------------
    # Cambiar zona
    # -------------------------


    def cambiar_zona(
        self,
        nueva_zona
    ):

        self.zona_actual = nueva_zona


        print(
            f"📍 Entraste a: {nueva_zona}"
        )



    # -------------------------
    # Recibir daño
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


        if self.vida == 0:

            self.estado = "Muerto"


            print(
                "☠️ Jugador eliminado"
            )



    # -------------------------
    # Curación
    # -------------------------


    def curar(
        self,
        cantidad
    ):


        self.vida += cantidad


        if self.vida > self.vida_maxima:

            self.vida = self.vida_maxima



        print(
            f"❤️ Vida recuperada: {cantidad}"
        )



    # -------------------------
    # Energía
    # -------------------------


    def descansar(
        self
    ):


        self.energia = self.energia_maxima


        print(
            "😴 Energía restaurada"
        )



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

            self.subir_nivel()



    def subir_nivel(
        self
    ):


        self.nivel += 1

        self.experiencia = 0


        print(
            f"🎉 Nuevo nivel: {self.nivel}"
        )



    # -------------------------
    # Estado del jugador
    # -------------------------


    def mostrar_estado(
        self
    ):


        print("=" * 50)

        print(
            f"🧍 JUGADOR: {self.nombre}"
        )

        print("=" * 50)


        print(
            f"❤️ Vida: {self.vida}/{self.vida_maxima}"
        )


        print(
            f"⚡ Energía: {self.energia}/{self.energia_maxima}"
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
            f"📍 Posición: {self.posicion}"
        )


        print(
            f"🌎 Zona: {self.zona_actual}"
        )


        print(
            f"Estado: {self.estado}"
        )