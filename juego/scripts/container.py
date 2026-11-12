# 🧟 SupervivenciaGame
# Sistema de Contenedores y Loot
# FASE 2.2 - Mundo con exploración real
# Versión v0.2.2


import random



class Contenedor:


    def __init__(
        self,
        nombre,
        tipo="Caja",
        cerrado=True
    ):

        self.nombre = nombre

        self.tipo = tipo

        self.cerrado = cerrado

        self.abierto = False

        self.objetos = []



    # -------------------------
    # Agregar objeto al contenedor
    # -------------------------


    def agregar_objeto(
        self,
        item
    ):


        self.objetos.append(
            item
        )



    # -------------------------
    # Abrir contenedor
    # -------------------------


    def abrir(
        self
    ):


        if self.abierto:


            print(
                f"📦 {self.nombre} ya está abierto"
            )

            return



        self.abierto = True

        self.cerrado = False


        print("=" * 50)

        print(
            f"📦 Abriendo: {self.nombre}"
        )

        print("=" * 50)



        if len(self.objetos) == 0:


            print(
                "❌ No hay nada dentro"
            )


        else:


            print(
                "🎁 Objetos encontrados:"
            )


            for item in self.objetos:


                print(
                    f"- {item.nombre} x{item.cantidad}"
                )



    # -------------------------
    # Saquear objeto
    # -------------------------


    def sacar_objeto(
        self,
        nombre
    ):


        for item in self.objetos:


            if item.nombre == nombre:


                self.objetos.remove(
                    item
                )


                print(
                    f"🎒 Sacaste: {item.nombre}"
                )


                return item



        print(
            "❌ Objeto no encontrado"
        )


        return None



    # -------------------------
    # Vaciar contenedor
    # -------------------------


    def saquear_todo(
        self
    ):


        objetos = self.objetos.copy()


        self.objetos.clear()



        print(
            f"🎒 Saqueados {len(objetos)} objetos"
        )


        return objetos



    # -------------------------
    # Generar loot aleatorio
    # -------------------------


    def generar_loot(
        self,
        posibles_objetos
    ):


        cantidad = random.randint(
            1,
            3
        )


        for i in range(
            cantidad
        ):


            objeto = random.choice(
                posibles_objetos
            )


            self.objetos.append(
                objeto
            )


        print(
            f"🎲 Loot generado en {self.nombre}"
        )



    # -------------------------
    # Mostrar contenido
    # -------------------------


    def mostrar(
        self
    ):


        print("=" * 50)

        print(
            f"📦 CONTENEDOR: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )

        print(
            f"Estado: {'Abierto' if self.abierto else 'Cerrado'}"
        )


        print("-" * 50)



        if len(self.objetos) == 0:


            print(
                "Vacío"
            )


        else:


            for item in self.objetos:


                print(
                    f"📦 {item.nombre} x{item.cantidad}"
                )


        print("=" * 50)