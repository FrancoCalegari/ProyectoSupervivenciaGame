# 🧟 SupervivenciaGame
# Sistema de Vehículos Abandonados
# FASE 2.3 - Mundo vivo
# Versión v0.2.3


class Vehiculo:


    def __init__(
        self,
        nombre,
        tipo="Auto"
    ):

        self.nombre = nombre

        self.tipo = tipo


        # Estado del vehículo

        self.estado = 100

        self.combustible = 0

        self.motor_funciona = False

        self.encendido = False


        # Inventario del vehículo

        self.maletero = []



    # -------------------------
    # Agregar objeto al maletero
    # -------------------------

    def agregar_objeto(
        self,
        item
    ):

        self.maletero.append(
            item
        )



    # -------------------------
    # Revisar vehículo
    # -------------------------

    def revisar(
        self
    ):

        print("=" * 60)

        print(
            f"🚗 VEHÍCULO: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print(
            f"Estado: {self.estado}%"
        )

        print(
            f"Combustible: {self.combustible}%"
        )

        print(
            f"Motor: {'Funciona' if self.motor_funciona else 'Roto'}"
        )


        print("=" * 60)



    # -------------------------
    # Revisar maletero
    # -------------------------

    def abrir_maletero(
        self
    ):


        print(
            f"\n📦 Maletero de {self.nombre}"
        )


        if len(self.maletero) == 0:


            print(
                "❌ Está vacío"
            )


        else:


            print(
                "🎁 Objetos encontrados:"
            )


            for item in self.maletero:


                print(
                    f"- {item.nombre} x{item.cantidad}"
                )



    # -------------------------
    # Sacar objeto
    # -------------------------

    def sacar_objeto(
        self,
        nombre
    ):


        for item in self.maletero:


            if item.nombre == nombre:


                self.maletero.remove(
                    item
                )


                print(
                    f"🎒 Sacaste {item.nombre}"
                )


                return item



        print(
            "❌ No encontrado"
        )


        return None



    # -------------------------
    # Cargar combustible
    # -------------------------

    def cargar_combustible(
        self,
        cantidad
    ):


        self.combustible += cantidad


        if self.combustible > 100:

            self.combustible = 100



        print(
            f"⛽ Combustible: {self.combustible}%"
        )



    # -------------------------
    # Reparar motor
    # -------------------------

    def reparar_motor(
        self
    ):


        self.motor_funciona = True


        print(
            "🔧 Motor reparado"
        )



    # -------------------------
    # Encender vehículo
    # -------------------------

    def encender(
        self
    ):


        if not self.motor_funciona:


            print(
                "❌ El motor no funciona"
            )

            return False



        if self.combustible <= 0:


            print(
                "❌ No hay combustible"
            )

            return False



        self.encendido = True


        print(
            "🚗 Vehículo encendido"
        )


        return True



    # -------------------------
    # Apagar vehículo
    # -------------------------

    def apagar(
        self
    ):


        self.encendido = False


        print(
            "🛑 Vehículo apagado"
        )