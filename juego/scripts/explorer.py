# 🧟 SupervivenciaGame
# Sistema de Exploración del Mundo
# FASE 2 - Mundo Jugable
# Versión v0.2.0


class Explorador:


    def __init__(
        self,
        jugador,
        mundo
    ):

        self.jugador = jugador

        self.mundo = mundo

        self.zona_actual = None



    # -------------------------
    # Iniciar exploración
    # -------------------------


    def iniciar_exploracion(
        self,
        zona_inicial
    ):


        zona = self.mundo.mapa.buscar_zona(
            zona_inicial
        )


        if zona:

            self.zona_actual = zona


            self.jugador.cambiar_zona(
                zona.nombre
            )


            print(
                f"🚀 Exploración iniciada en: {zona.nombre}"
            )


        else:

            print(
                "❌ Zona inicial no encontrada"
            )



    # -------------------------
    # Mover entre zonas
    # -------------------------


    def viajar(
        self,
        destino
    ):


        zona = self.mundo.mapa.buscar_zona(
            destino
        )


        if zona:


            print("=" * 50)

            print(
                f"🚶 Viajando hacia: {destino}"
            )

            print("=" * 50)


            self.zona_actual = zona


            self.jugador.cambiar_zona(
                zona.nombre
            )


            self.mostrar_zona()



        else:

            print(
                "❌ No existe esa zona"
            )



    # -------------------------
    # Mostrar zona actual
    # -------------------------


    def mostrar_zona(
        self
    ):


        if self.zona_actual is None:

            print(
                "❌ No estás en ninguna zona"
            )

            return



        print("\n" + "=" * 50)

        print(
            f"📍 ZONA ACTUAL: {self.zona_actual.nombre}"
        )

        print("=" * 50)


        print(
            f"🌎 Tipo: {self.zona_actual.tipo}"
        )


        print(
            f"📝 {self.zona_actual.descripcion}"
        )



        print("\n🌲 Recursos encontrados:")


        if len(self.zona_actual.recursos) == 0:

            print(
                "Ninguno"
            )

        else:

            for recurso in self.zona_actual.recursos:

                print(
                    f" - {recurso}"
                )



        print("\n🏠 Edificios:")


        if len(self.zona_actual.edificios) == 0:

            print(
                "Ninguno"
            )

        else:

            for edificio in self.zona_actual.edificios:

                print(
                    f" - {edificio}"
                )



        print("\n🧟 Amenazas:")


        if len(self.zona_actual.zombies) == 0:

            print(
                "Sin zombies detectados"
            )

        else:

            for zombie in self.zona_actual.zombies:

                print(
                    f" - {zombie}"
                )



    # -------------------------
    # Buscar recursos
    # -------------------------


    def buscar_recursos(
        self
    ):


        if self.zona_actual is None:

            print(
                "❌ No hay zona seleccionada"
            )

            return



        print(
            "🔎 Buscando recursos..."
        )


        for recurso in self.zona_actual.recursos:

            print(
                f"🌲 Encontrado: {recurso}"
            )



    # -------------------------
    # Detectar peligro
    # -------------------------


    def detectar_peligros(
        self
    ):


        if self.zona_actual is None:

            return



        cantidad = len(
            self.zona_actual.zombies
        )


        if cantidad > 0:


            print(
                f"⚠️ Peligro: {cantidad} zombies en la zona"
            )


        else:

            print(
                "✅ Zona segura"
            )