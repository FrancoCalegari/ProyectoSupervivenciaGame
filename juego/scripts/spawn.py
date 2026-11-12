# 🧟 SupervivenciaGame
# Sistema de aparición de enemigos y entidades
# FASE 2 - Mundo Jugable
# Versión v0.2.0


import random



class SistemaSpawn:


    def __init__(
        self,
        mundo
    ):

        self.mundo = mundo

        self.zombies_generados = 0



    # -------------------------
    # Crear zombies en una zona
    # -------------------------


    def generar_zombies(
        self,
        nombre_zona,
        cantidad
    ):


        zona = self.mundo.mapa.buscar_zona(
            nombre_zona
        )


        if zona is None:

            print(
                "❌ Zona no encontrada"
            )

            return



        print("=" * 50)

        print(
            f"🧟 Generando zombies en: {nombre_zona}"
        )

        print("=" * 50)



        for i in range(cantidad):


            tipo = self.elegir_tipo_zombie()


            zombie = {

                "id": self.zombies_generados + 1,

                "tipo": tipo,

                "vida": self.vida_zombie(tipo),

                "daño": self.danio_zombie(tipo)

            }



            zona.agregar_zombie(
                zombie
            )


            self.mundo.agregar_zombie(
                zombie
            )


            self.zombies_generados += 1



            print(
                f"🧟 Zombie creado: {tipo}"
            )



    # -------------------------
    # Tipos de zombies
    # -------------------------


    def elegir_tipo_zombie(
        self
    ):


        tipos = [

            "Comun",

            "Comun",

            "Corredor",

            "Fuerte"

        ]


        return random.choice(
            tipos
        )



    # -------------------------
    # Estadísticas
    # -------------------------


    def vida_zombie(
        self,
        tipo
    ):


        if tipo == "Fuerte":

            return 200



        if tipo == "Corredor":

            return 80



        return 100



    def danio_zombie(
        self,
        tipo
    ):


        if tipo == "Fuerte":

            return 25



        if tipo == "Corredor":

            return 15



        return 10



    # -------------------------
    # Spawn automático por zona
    # -------------------------


    def generar_mundo_inicial(
        self
    ):


        print(
            "🌎 Generando amenazas del mundo..."
        )


        self.generar_zombies(
            "Casa abandonada",
            2
        )


        self.generar_zombies(
            "Bosque",
            3
        )


        self.generar_zombies(
            "Ciudad abandonada",
            6
        )


        print(
            "✅ Spawn inicial completado"
        )



    # -------------------------
    # Mostrar zombies
    # -------------------------


    def mostrar_zombies(
        self
    ):


        print("=" * 50)

        print(
            "🧟 ZOMBIES DEL MUNDO"
        )

        print("=" * 50)



        for zombie in self.mundo.zombies:


            print(
                f"ID: {zombie['id']} | "
                f"Tipo: {zombie['tipo']} | "
                f"Vida: {zombie['vida']} | "
                f"Daño: {zombie['daño']}"
            )