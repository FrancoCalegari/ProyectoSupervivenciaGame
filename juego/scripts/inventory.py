# 🧟 SupervivenciaGame
# Sistema de Inventario
# Versión: v0.1.1


class Objeto:

    def __init__(
        self,
        nombre,
        tipo,
        peso,
        cantidad=1
    ):

        self.nombre = nombre
        self.tipo = tipo
        self.peso = peso
        self.cantidad = cantidad



    def mostrar(self):

        print(
            f"📦 {self.nombre} "
            f"x{self.cantidad} "
            f"| Peso: {self.peso}"
        )



class Inventario:


    def __init__(
        self,
        capacidad=20
    ):

        # Cantidad máxima de espacios
        self.capacidad = capacidad

        # Lista de objetos
        self.objetos = []



    def mostrar_inventario(self):

        print("=" * 45)
        print("🎒 INVENTARIO")
        print("=" * 45)


        if len(self.objetos) == 0:

            print(
                "Inventario vacío"
            )

            return


        for objeto in self.objetos:

            objeto.mostrar()



        print(
            "\nEspacios usados:",
            len(self.objetos),
            "/",
            self.capacidad
        )



    def agregar_objeto(
        self,
        objeto
    ):


        if len(self.objetos) >= self.capacidad:

            print(
                "❌ Inventario lleno"
            )

            return False



        # Revisar si ya existe
        for item in self.objetos:

            if item.nombre == objeto.nombre:

                item.cantidad += objeto.cantidad

                print(
                    f"➕ {objeto.nombre} agregado"
                )

                return True



        self.objetos.append(
            objeto
        )


        print(
            f"📦 Nuevo objeto:"
            f" {objeto.nombre}"
        )


        return True



    def quitar_objeto(
        self,
        nombre,
        cantidad=1
    ):


        for objeto in self.objetos:


            if objeto.nombre == nombre:


                objeto.cantidad -= cantidad


                print(
                    f"➖ Quitado:"
                    f" {nombre}"
                )


                if objeto.cantidad <= 0:

                    self.objetos.remove(
                        objeto
                    )


                return True



        print(
            "❌ Objeto no encontrado"
        )


        return False



    def buscar_objeto(
        self,
        nombre
    ):


        for objeto in self.objetos:


            if objeto.nombre == nombre:

                return objeto



        return None



    def usar_objeto(
        self,
        nombre
    ):


        objeto = self.buscar_objeto(
            nombre
        )


        if objeto:


            print(
                f"🖐️ Usando {nombre}"
            )


            self.quitar_objeto(
                nombre
            )


        else:


            print(
                "❌ No tienes ese objeto"
            )



    def peso_total(self):


        peso = 0


        for objeto in self.objetos:

            peso += (
                objeto.peso *
                objeto.cantidad
            )


        return peso