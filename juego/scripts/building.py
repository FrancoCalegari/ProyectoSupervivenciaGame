# 🧟 SupervivenciaGame
# Sistema de Edificios Explorables
# FASE 2.3 - Mundo vivo
# Versión v0.2.3


class Edificio:


    def __init__(
        self,
        nombre,
        tipo="Casa"
    ):

        self.nombre = nombre

        self.tipo = tipo

        self.explorado = False

        self.habitaciones = []

        self.contenedores = []

        self.estado = "Abandonado"



    # -------------------------
    # Agregar habitación
    # -------------------------

    def agregar_habitacion(
        self,
        habitacion
    ):

        self.habitaciones.append(
            habitacion
        )



    # -------------------------
    # Agregar contenedor
    # -------------------------

    def agregar_contenedor(
        self,
        contenedor
    ):

        self.contenedores.append(
            contenedor
        )



    # -------------------------
    # Explorar edificio
    # -------------------------

    def explorar(
        self
    ):


        if self.explorado:

            print(
                f"🏠 {self.nombre} ya fue explorado"
            )

            return



        self.explorado = True


        print("=" * 60)

        print(
            f"🏠 Explorando: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print("=" * 60)



        if len(self.habitaciones) > 0:


            print("\n🚪 Habitaciones:")


            for habitacion in self.habitaciones:

                print(
                    f"- {habitacion}"
                )



        if len(self.contenedores) > 0:


            print("\n📦 Contenedores encontrados:")


            for contenedor in self.contenedores:

                print(
                    f"- {contenedor.nombre}"
                )



        else:

            print(
                "\n❌ No hay contenedores"
            )



    # -------------------------
    # Buscar loot
    # -------------------------

    def abrir_contenedores(
        self
    ):


        print(
            f"\n📦 Revisando objetos en {self.nombre}"
        )



        for contenedor in self.contenedores:


            contenedor.abrir()



    # -------------------------
    # Mostrar información
    # -------------------------

    def mostrar(
        self
    ):


        print("=" * 60)

        print(
            f"🏠 EDIFICIO: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print(
            f"Estado: {self.estado}"
        )

        print(
            f"Explorado: {'Sí' if self.explorado else 'No'}"
        )


        print("=" * 60)