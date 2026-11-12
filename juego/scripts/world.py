# 🧟 SupervivenciaGame
# Sistema Principal del Mundo
# FASE 2 - Mundo Jugable
# Versión v0.2.0


from location import Localizacion, Mapa



class Mundo:


    def __init__(
        self,
        nombre
    ):

        self.nombre = nombre

        self.mapa = Mapa(
            nombre
        )

        self.dia = 1
        self.hora = 8
        self.clima = "Despejado"

        self.jugador = None

        self.zombies = []



    def iniciar_mundo(self):

        print("=" * 50)
        print(
            f"🌎 Iniciando mundo: {self.nombre}"
        )
        print("=" * 50)


        self.crear_zonas()


        print(
            "✅ Mundo creado correctamente"
        )



    def crear_zonas(self):


        casa = Localizacion(

            "Casa abandonada",

            "Edificio",

            "Una casa vieja con recursos y peligros."

        )


        casa.agregar_recurso(
            "Tela"
        )

        casa.agregar_recurso(
            "Comida"
        )

        casa.agregar_edificio(
            "Casa pequeña"
        )



        bosque = Localizacion(

            "Bosque",

            "Zona natural",

            "Zona con árboles y materiales."

        )


        bosque.agregar_recurso(
            "Madera"
        )

        bosque.agregar_recurso(
            "Piedra"
        )



        ciudad = Localizacion(

            "Ciudad abandonada",

            "Zona urbana",

            "Calles peligrosas llenas de edificios."

        )


        ciudad.agregar_recurso(
            "Metal"
        )


        ciudad.agregar_edificio(
            "Edificio comercial"
        )



        self.mapa.agregar_zona(
            casa
        )


        self.mapa.agregar_zona(
            bosque
        )


        self.mapa.agregar_zona(
            ciudad
        )



    def colocar_jugador(
        self,
        jugador
    ):

        self.jugador = jugador


        print(
            f"🧍 Jugador colocado: {jugador.nombre}"
        )



    def agregar_zombie(
        self,
        zombie
    ):

        self.zombies.append(
            zombie
        )


        print(
            "🧟 Zombie agregado al mundo"
        )



    def entrar_zona(
        self,
        nombre
    ):


        zona = self.mapa.buscar_zona(
            nombre
        )


        if zona:

            zona.entrar()

        else:

            print(
                "❌ Zona no encontrada"
            )



    def cambiar_hora(
        self
    ):

        self.hora += 1


        if self.hora >= 24:

            self.hora = 0

            self.dia += 1


            print(
                f"🌅 Día nuevo: {self.dia}"
            )



    def cambiar_clima(
        self,
        clima
    ):

        self.clima = clima


        print(
            f"🌦️ Clima cambiado: {clima}"
        )



    def mostrar_estado(
        self
    ):


        print("=" * 50)

        print(
            f"🌎 Mundo: {self.nombre}"
        )

        print(
            f"📅 Día: {self.dia}"
        )

        print(
            f"🕒 Hora: {self.hora}:00"
        )

        print(
            f"🌤️ Clima: {self.clima}"
        )


        print(
            f"🧟 Zombies: {len(self.zombies)}"
        )


        if self.jugador:

            print(
                f"🧍 Jugador: {self.jugador.nombre}"
            )


        print()


        self.mapa.mostrar_mapa()