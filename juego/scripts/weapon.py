# 🧟 SupervivenciaGame
# Sistema de Armas
# Versión: v0.1.1


class Arma:

    def __init__(
        self,
        nombre,
        tipo,
        daño,
        capacidad_cargador
    ):

        # Información del arma
        self.nombre = nombre
        self.tipo = tipo

        # Estadísticas
        self.daño = daño
        self.capacidad_cargador = capacidad_cargador
        self.municion_actual = capacidad_cargador

        # Estado
        self.durabilidad = 100
        self.estado = "Operativa"


    def mostrar_estado(self):

        print("=" * 40)
        print("🔫 ESTADO DEL ARMA")
        print("=" * 40)

        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Daño: {self.daño}")

        print(
            f"Munición: {self.municion_actual}/"
            f"{self.capacidad_cargador}"
        )

        print(
            f"Durabilidad: {self.durabilidad}%"
        )

        print(
            f"Estado: {self.estado}"
        )


    def disparar(self, objetivo):

        if self.estado != "Operativa":

            print(
                "❌ El arma no funciona"
            )

            return


        if self.municion_actual <= 0:

            print(
                "🔴 Sin munición, necesita recarga"
            )

            return


        self.municion_actual -= 1

        print(
            f"💥 {self.nombre} disparó"
        )

        objetivo.recibir_daño(
            self.daño
        )

        self.reducir_durabilidad(1)


    def recargar(self):

        self.municion_actual = (
            self.capacidad_cargador
        )

        print(
            f"🔄 {self.nombre} recargada"
        )


    def reducir_durabilidad(self, cantidad):

        self.durabilidad -= cantidad


        if self.durabilidad <= 0:

            self.durabilidad = 0
            self.estado = "Rota"

            print(
                "⚠️ El arma se rompió"
            )


    def reparar(self, cantidad):

        self.durabilidad += cantidad


        if self.durabilidad > 100:

            self.durabilidad = 100


        if self.durabilidad > 0:

            self.estado = "Operativa"


        print(
            "🔧 Arma reparada"
        )



# Armas especiales


class Pistola(Arma):

    def __init__(self):

        super().__init__(
            "Pistola M9",
            "Pistola",
            25,
            15
        )



class Rifle(Arma):

    def __init__(self):

        super().__init__(
            "Rifle de Asalto",
            "Rifle",
            45,
            30
        )



class Escopeta(Arma):

    def __init__(self):

        super().__init__(
            "Escopeta Táctica",
            "Escopeta",
            80,
            8
        )



class Francotirador(Arma):

    def __init__(self):

        super().__init__(
            "Rifle Francotirador",
            "Precisión",
            120,
            5
        )