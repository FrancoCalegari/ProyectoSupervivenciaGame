# 🧟 SupervivenciaGame
# Sistema de Recursos y Recolección
# Versión: v0.1.1


class Recurso:

    def __init__(
        self,
        nombre,
        tipo,
        cantidad,
        maximo
    ):

        self.nombre = nombre
        self.tipo = tipo

        # Cantidad disponible
        self.cantidad = cantidad

        # Cantidad máxima
        self.maximo = maximo

        self.estado = "Disponible"



    def recolectar(
        self,
        cantidad
    ):

        if self.cantidad <= 0:

            self.estado = "Agotado"

            print(
                f"❌ {self.nombre} agotado"
            )

            return 0



        if cantidad > self.cantidad:

            cantidad = self.cantidad



        self.cantidad -= cantidad


        print(
            f"🌿 Recolectado {cantidad} "
            f"de {self.nombre}"
        )


        if self.cantidad == 0:

            self.estado = "Agotado"

            print(
                f"⚠️ {self.nombre} se agotó"
            )


        return cantidad



    def restaurar(self):

        self.cantidad = self.maximo
        self.estado = "Disponible"


        print(
            f"♻️ {self.nombre} restaurado"
        )



    def mostrar_estado(self):

        print("=" * 40)

        print(
            f"🌎 Recurso: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print(
            f"Cantidad: {self.cantidad}/{self.maximo}"
        )

        print(
            f"Estado: {self.estado}"
        )



class SistemaRecursos:


    def __init__(
        self,
        inventario
    ):

        self.inventario = inventario

        self.recursos = []

        self.crear_recursos()



    def crear_recursos(self):


        self.recursos.append(

            Recurso(
                "Árbol",
                "Madera",
                10,
                10
            )

        )


        self.recursos.append(

            Recurso(
                "Chatarra",
                "Metal",
                8,
                8
            )

        )


        self.recursos.append(

            Recurso(
                "Roca",
                "Piedra",
                15,
                15
            )

        )


        self.recursos.append(

            Recurso(
                "Caja de comida",
                "Comida",
                5,
                5
            )

        )


        self.recursos.append(

            Recurso(
                "Tela abandonada",
                "Tela",
                6,
                6
            )

        )



    def mostrar_recursos(self):

        print("=" * 45)
        print("🌎 RECURSOS DEL MAPA")
        print("=" * 45)


        for recurso in self.recursos:

            print(
                f"- {recurso.nombre}"
                f" | {recurso.tipo}"
                f" | Cantidad: {recurso.cantidad}"
            )



    def buscar_recurso(
        self,
        nombre
    ):


        for recurso in self.recursos:

            if recurso.nombre == nombre:

                return recurso



        return None



    def recolectar_recurso(
        self,
        nombre,
        cantidad
    ):


        recurso = self.buscar_recurso(
            nombre
        )


        if recurso is None:

            print(
                "❌ Recurso no encontrado"
            )

            return False



        obtenido = recurso.recolectar(
            cantidad
        )


        if obtenido > 0:


            from inventory import Objeto


            objeto = Objeto(

                recurso.tipo,

                "Material",

                1,

                obtenido

            )


            self.inventario.agregar_objeto(
                objeto
            )


            print(
                f"📦 Añadido al inventario: "
                f"{recurso.tipo} x{obtenido}"
            )


            return True



        return False



    def restaurar_todos(self):

        print(
            "♻️ Restaurando recursos del mapa..."
        )


        for recurso in self.recursos:

            recurso.restaurar()


        print(
            "✅ Recursos restaurados"
        )