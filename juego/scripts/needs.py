# 🧟 SupervivenciaGame
# Sistema de Necesidades del Superviviente
# FASE 2.4 - Supervivencia avanzada
# Versión v0.2.4


class Necesidades:


    def __init__(
        self
    ):

        # Valores del jugador

        self.hambre = 100

        self.sed = 100

        self.energia = 100

        self.temperatura = 100

        self.fatiga = 0


        # Estados

        self.estado = "Normal"



    # -------------------------
    # Pasar tiempo
    # -------------------------

    def pasar_tiempo(
        self,
        horas=1
    ):


        self.hambre -= 5 * horas

        self.sed -= 8 * horas

        self.energia -= 4 * horas

        self.fatiga += 5 * horas



        self.limitar_valores()


        self.actualizar_estado()



    # -------------------------
    # Comer
    # -------------------------

    def comer(
        self,
        cantidad=20
    ):


        self.hambre += cantidad


        if self.hambre > 100:

            self.hambre = 100



        print(
            f"🍖 Hambre recuperada +{cantidad}"
        )



    # -------------------------
    # Beber
    # -------------------------

    def beber(
        self,
        cantidad=30
    ):


        self.sed += cantidad


        if self.sed > 100:

            self.sed = 100



        print(
            f"💧 Sed recuperada +{cantidad}"
        )



    # -------------------------
    # Dormir
    # -------------------------

    def dormir(
        self,
        horas=8
    ):


        self.energia += 10 * horas

        self.fatiga -= 10 * horas



        self.limitar_valores()



        print(
            "😴 El superviviente descansó"
        )



    # -------------------------
    # Temperatura
    # -------------------------

    def cambiar_temperatura(
        self,
        valor
    ):


        self.temperatura += valor


        self.limitar_valores()



    # -------------------------
    # Limitar valores
    # -------------------------

    def limitar_valores(
        self
    ):


        valores = [

            "hambre",

            "sed",

            "energia",

            "temperatura"

        ]


        for valor in valores:


            actual = getattr(
                self,
                valor
            )


            if actual < 0:

                setattr(
                    self,
                    valor,
                    0
                )


            if actual > 100:

                setattr(
                    self,
                    valor,
                    100
                )



        if self.fatiga < 0:

            self.fatiga = 0



    # -------------------------
    # Estado del jugador
    # -------------------------

    def actualizar_estado(
        self
    ):


        if self.hambre <= 20:

            self.estado = "Hambriento"



        elif self.sed <= 20:

            self.estado = "Deshidratado"



        elif self.energia <= 20:

            self.estado = "Agotado"



        elif self.fatiga >= 80:

            self.estado = "Muy cansado"



        else:

            self.estado = "Normal"



    # -------------------------
    # Mostrar
    # -------------------------

    def mostrar(
        self
    ):


        print("=" * 50)

        print(
            "🥩 NECESIDADES DEL SUPERVIVIENTE"
        )

        print("-" * 50)

        print(
            f"🍖 Hambre: {self.hambre}%"
        )

        print(
            f"💧 Sed: {self.sed}%"
        )

        print(
            f"⚡ Energía: {self.energia}%"
        )

        print(
            f"🌡️ Temperatura: {self.temperatura}%"
        )

        print(
            f"😴 Fatiga: {self.fatiga}%"
        )

        print(
            f"⚠️ Estado: {self.estado}"
        )

        print("=" * 50)