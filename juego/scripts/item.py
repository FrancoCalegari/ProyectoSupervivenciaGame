# 🧟 SupervivenciaGame
# Sistema base de objetos
# FASE 2.1


class Item:


    def __init__(
        self,
        nombre,
        tipo,
        peso,
        cantidad=1,
        rareza="Común",
        apilable=True,
        estado=100
    ):

        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
        self.cantidad = cantidad
        self.rareza = rareza
        self.apilable = apilable
        self.estado = estado



    def peso_total(
        self
    ):

        return self.peso * self.cantidad



    def agregar(
        self,
        cantidad
    ):

        if self.apilable:

            self.cantidad += cantidad

            print(
                f"➕ {self.nombre} +{cantidad}"
            )



    def quitar(
        self,
        cantidad
    ):

        if cantidad > self.cantidad:

            return False


        self.cantidad -= cantidad

        return True



    def desgastar(
        self,
        cantidad
    ):

        self.estado -= cantidad


        if self.estado < 0:

            self.estado = 0



    def reparar(
        self
    ):

        self.estado = 100



    def mostrar(
        self
    ):

        print("=" * 40)

        print(
            f"📦 {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print(
            f"Cantidad: {self.cantidad}"
        )

        print(
            f"Peso total: {self.peso_total()} kg"
        )

        print(
            f"Rareza: {self.rareza}"
        )

        print(
            f"Estado: {self.estado}%"
        )



    def to_dict(
        self
    ):

        return {

            "nombre": self.nombre,
            "tipo": self.tipo,
            "peso": self.peso,
            "cantidad": self.cantidad,
            "rareza": self.rareza,
            "apilable": self.apilable,
            "estado": self.estado

        }



    @classmethod
    def from_dict(
        cls,
        datos
    ):

        return cls(

            datos["nombre"],
            datos["tipo"],
            datos["peso"],
            datos["cantidad"],
            datos["rareza"],
            datos["apilable"],
            datos["estado"]

        )