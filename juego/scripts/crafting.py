# 🧟 SupervivenciaGame
# Sistema de Fabricación (Crafting)
# Versión: v0.1.1


class Receta:


    def __init__(
        self,
        nombre,
        materiales,
        resultado
    ):

        self.nombre = nombre

        # Diccionario:
        # material : cantidad
        self.materiales = materiales

        self.resultado = resultado



    def mostrar_receta(self):

        print("=" * 40)
        print(f"🛠️ Receta: {self.nombre}")
        print("=" * 40)

        print("Materiales:")

        for material, cantidad in self.materiales.items():

            print(
                f"- {material}: {cantidad}"
            )


        print(
            f"Resultado: {self.resultado}"
        )



class SistemaCrafting:


    def __init__(
        self,
        inventario
    ):

        self.inventario = inventario

        self.recetas = []

        self.crear_recetas()



    def crear_recetas(self):


        # 🩹 Venda

        venda = Receta(

            "Venda",

            {
                "Tela": 2,
                "Alcohol": 1
            },

            "Venda"
        )


        # 🔪 Cuchillo

        cuchillo = Receta(

            "Cuchillo",

            {
                "Metal": 2,
                "Cinta": 1
            },

            "Cuchillo"
        )



        # 🧨 Molotov

        molotov = Receta(

            "Molotov",

            {
                "Botella": 1,
                "Alcohol": 1,
                "Tela": 1
            },

            "Molotov"
        )



        # 🔧 Reparación

        reparacion = Receta(

            "Kit de reparación",

            {
                "Metal": 3,
                "Herramienta": 1
            },

            "Kit Reparación"
        )



        self.recetas.append(venda)
        self.recetas.append(cuchillo)
        self.recetas.append(molotov)
        self.recetas.append(reparacion)



    def mostrar_recetas(self):


        print("=" * 45)
        print("🛠️ RECETAS DISPONIBLES")
        print("=" * 45)


        for receta in self.recetas:

            print(
                "-",
                receta.nombre
            )



    def buscar_receta(
        self,
        nombre
    ):


        for receta in self.recetas:

            if receta.nombre == nombre:

                return receta


        return None



    def comprobar_materiales(
        self,
        receta
    ):


        for material, cantidad in receta.materiales.items():


            objeto = (
                self.inventario.buscar_objeto(
                    material
                )
            )


            if objeto is None:

                return False


            if objeto.cantidad < cantidad:

                return False



        return True



    def fabricar(
        self,
        nombre_receta
    ):


        receta = self.buscar_receta(
            nombre_receta
        )


        if receta is None:


            print(
                "❌ Receta no encontrada"
            )


            return False



        if not self.comprobar_materiales(
            receta
        ):


            print(
                "❌ Faltan materiales"
            )


            return False



        # Consumir materiales

        for material, cantidad in receta.materiales.items():


            self.inventario.quitar_objeto(
                material,
                cantidad
            )



        # Crear objeto nuevo

        from inventory import Objeto


        nuevo_objeto = Objeto(

            receta.resultado,

            "Fabricado",

            1

        )


        self.inventario.agregar_objeto(
            nuevo_objeto
        )


        print(
            f"✅ Fabricado: {receta.resultado}"
        )


        return True