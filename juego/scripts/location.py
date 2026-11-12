# 🧟 SupervivenciaGame
# Sistema de Localizaciones del Mundo
# FASE 2 - Mundo Jugable
# Versión v0.2.0


class Localizacion:


    def __init__(
        self,
        nombre,
        tipo,
        descripcion
    ):

        self.nombre = nombre

        # Tipo de zona:
        # Casa, Bosque, Ciudad, etc.
        self.tipo = tipo

        self.descripcion = descripcion


        # Objetos dentro de la zona

        self.recursos = []

        self.zombies = []

        self.edificios = []

        self.visitada = False



    def entrar(self):

        self.visitada = True


        print("=" * 50)
        print(f"📍 Entrando a: {self.nombre}")
        print("=" * 50)


        print(
            f"🌎 Tipo: {self.tipo}"
        )


        print(
            f"📝 {self.descripcion}"
        )



    def agregar_recurso(
        self,
        recurso
    ):

        self.recursos.append(
            recurso
        )


        print(
            f"🌲 Recurso agregado: {recurso}"
        )



    def agregar_zombie(
        self,
        zombie
    ):

        self.zombies.append(
            zombie
        )


        print(
            f"🧟 Zombie agregado a {self.nombre}"
        )



    def agregar_edificio(
        self,
        edificio
    ):

        self.edificios.append(
            edificio
        )


        print(
            f"🏠 Edificio agregado: {edificio}"
        )



    def mostrar_estado(
        self
    ):

        print("\n" + "=" * 50)

        print(
            f"📍 ZONA: {self.nombre}"
        )

        print(
            f"Tipo: {self.tipo}"
        )


        print(
            f"Visitada: {self.visitada}"
        )


        print("\n🌲 Recursos:")

        if len(self.recursos) == 0:

            print(
                "Ninguno"
            )

        else:

            for recurso in self.recursos:

                print(
                    f"- {recurso}"
                )



        print("\n🧟 Zombies:")

        if len(self.zombies) == 0:

            print(
                "Ninguno"
            )

        else:

            for zombie in self.zombies:

                print(
                    f"- {zombie}"
                )



        print("\n🏠 Edificios:")

        if len(self.edificios) == 0:

            print(
                "Ninguno"
            )

        else:

            for edificio in self.edificios:

                print(
                    f"- {edificio}"
                )



        print("=" * 50)



class Mapa:


    def __init__(
        self,
        nombre
    ):

        self.nombre = nombre

        self.localizaciones = []



    def agregar_zona(
        self,
        zona
    ):

        self.localizaciones.append(
            zona
        )


        print(
            f"🗺️ Zona agregada: {zona.nombre}"
        )



    def buscar_zona(
        self,
        nombre
    ):


        for zona in self.localizaciones:


            if zona.nombre == nombre:

                return zona



        return None



    def mostrar_mapa(
        self
    ):

        print("=" * 50)

        print(
            f"🗺️ MAPA: {self.nombre}"
        )

        print("=" * 50)


        for zona in self.localizaciones:

            print(
                f"📍 {zona.nombre} - {zona.tipo}"
            )