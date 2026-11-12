# 🧟 SupervivenciaGame
# Sistema Inventario conectado con Item
# FASE 2.2


class Inventario:


    def __init__(
        self,
        peso_maximo=30
    ):

        self.items = []

        self.peso_maximo = peso_maximo



    # -------------------------
    # Peso actual
    # -------------------------

    def peso_actual(
        self
    ):

        peso = 0


        for item in self.items:

            peso += item.peso_total()


        return peso



    # -------------------------
    # Agregar objeto
    # -------------------------

    def agregar_item(
        self,
        item
    ):


        if self.peso_actual() + item.peso_total() > self.peso_maximo:


            print(
                "❌ Inventario lleno"
            )

            return False



        for existente in self.items:


            if (
                existente.nombre == item.nombre
                and existente.apilable
            ):

                existente.agregar(
                    item.cantidad
                )

                return True



        self.items.append(
            item
        )


        print(
            f"🎒 Objeto agregado: {item.nombre}"
        )


        return True



    # -------------------------
    # Buscar objeto
    # -------------------------

    def buscar(
        self,
        nombre
    ):


        for item in self.items:


            if item.nombre == nombre:

                return item


        return None



    # -------------------------
    # Quitar objeto
    # -------------------------

    def quitar_item(
        self,
        nombre,
        cantidad=1
    ):


        item = self.buscar(
            nombre
        )


        if item is None:

            return False



        eliminado = item.quitar(
            cantidad
        )


        if eliminado and item.cantidad <= 0:

            self.items.remove(
                item
            )


        return eliminado



    # -------------------------
    # Mostrar inventario
    # -------------------------

    def mostrar(
        self
    ):


        print("=" * 50)

        print(
            "🎒 INVENTARIO"
        )

        print("=" * 50)



        if len(self.items) == 0:


            print(
                "Vacío"
            )


        else:


            for item in self.items:


                print(
                    f"📦 {item.nombre} x{item.cantidad} | {item.peso_total()} kg"
                )



        print(
            "-" * 50
        )


        print(
            f"⚖️ Peso: {self.peso_actual()} / {self.peso_maximo} kg"
        )



    # -------------------------
    # Guardar
    # -------------------------

    def to_dict(
        self
    ):


        return {

            "peso_maximo": self.peso_maximo,

            "items": [

                item.to_dict()

                for item in self.items

            ]

        }