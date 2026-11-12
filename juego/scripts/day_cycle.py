# 🧟 SupervivenciaGame
# Sistema Ciclo Día/Noche
# FASE 2.4 - Supervivencia avanzada
# Versión v0.2.4


class CicloDia:


    def __init__(
        self
    ):

        self.dia = 1

        self.hora = 6

        self.minutos = 0

        self.estado = "Mañana"



    # -------------------------
    # Avanzar tiempo
    # -------------------------

    def avanzar_tiempo(
        self,
        horas=1
    ):

        self.hora += horas


        while self.hora >= 24:

            self.hora -= 24

            self.dia += 1



        self.actualizar_estado()



    # -------------------------
    # Actualizar momento del día
    # -------------------------

    def actualizar_estado(
        self
    ):


        if self.hora >= 6 and self.hora < 12:

            self.estado = "Mañana"



        elif self.hora >= 12 and self.hora < 18:

            self.estado = "Día"



        elif self.hora >= 18 and self.hora < 21:

            self.estado = "Atardecer"



        else:

            self.estado = "Noche"



    # -------------------------
    # Obtener hora
    # -------------------------

    def obtener_hora(
        self
    ):

        return (
            f"Día {self.dia} "
            f"{self.hora:02d}:{self.minutos:02d}"
        )



    # -------------------------
    # Mostrar información
    # -------------------------

    def mostrar(
        self
    ):

        print("=" * 50)

        print(
            "🌞 CICLO DEL MUNDO"
        )

        print("-" * 50)

        print(
            f"📅 {self.obtener_hora()}"
        )

        print(
            f"🌎 Estado: {self.estado}"
        )


        if self.estado == "Noche":

            print(
                "🧟 El peligro aumenta..."
            )


        print("=" * 50)