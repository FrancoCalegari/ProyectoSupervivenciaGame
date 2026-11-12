# 🧟 SupervivenciaGame
# Sistema de Interacción con el Mundo
# FASE 2 - Mundo Jugable
# Versión v0.2.0


class SistemaInteraccion:


    def __init__(
        self,
        jugador,
        mundo
    ):

        self.jugador = jugador

        self.mundo = mundo

        self.zona_actual = None



    # -------------------------
    # Seleccionar zona
    # -------------------------


    def cambiar_zona(
        self,
        nombre_zona
    ):


        zona = self.mundo.mapa.buscar_zona(
            nombre_zona
        )


        if zona:

            self.zona_actual = zona


            self.jugador.cambiar_zona(
                zona.nombre
            )


            print(
                f"📍 Interacción iniciada en: {zona.nombre}"
            )


        else:

            print(
                "❌ Zona no encontrada"
            )



    # -------------------------
    # Revisar zona
    # -------------------------


    def revisar_zona(
        self
    ):


        if self.zona_actual is None:

            print(
                "❌ No hay zona seleccionada"
            )

            return



        print("=" * 50)

        print(
            f"🔎 Revisando: {self.zona_actual.nombre}"
        )

        print("=" * 50)



        print(
            "🌲 Recursos disponibles:"
        )


        if len(self.zona_actual.recursos) == 0:

            print(
                "Ninguno"
            )

        else:

            for recurso in self.zona_actual.recursos:

                print(
                    f"- {recurso}"
                )



        print(
            "\n🏠 Edificios:"
        )


        if len(self.zona_actual.edificios) == 0:

            print(
                "Ninguno"
            )

        else:

            for edificio in self.zona_actual.edificios:

                print(
                    f"- {edificio}"
                )



    # -------------------------
    # Recoger recursos
    # -------------------------


    def recoger_recurso(
        self,
        recurso
    ):


        if self.zona_actual is None:

            print(
                "❌ No hay zona seleccionada"
            )

            return



        if recurso in self.zona_actual.recursos:


            self.zona_actual.recursos.remove(
                recurso
            )


            print(
                f"🎒 Recurso recogido: {recurso}"
            )


            # Si existe inventario

            if hasattr(
                self.jugador,
                "inventario"
            ):

                self.jugador.inventario.agregar_item(
                    recurso
                )


            else:

                print(
                    "📦 Recurso guardado temporalmente"
                )



        else:

            print(
                f"❌ No existe {recurso} en esta zona"
            )



    # -------------------------
    # Revisar edificios
    # -------------------------


    def entrar_edificio(
        self,
        edificio
    ):


        if self.zona_actual is None:

            print(
                "❌ No estás en ninguna zona"
            )

            return



        if edificio in self.zona_actual.edificios:


            print("=" * 50)

            print(
                f"🏠 Entrando a: {edificio}"
            )

            print("=" * 50)


            print(
                "🔎 Buscando objetos..."
            )


            objetos = [

                "Comida",

                "Agua",

                "Munición",

                "Medicamentos"

            ]


            for objeto in objetos:

                print(
                    f"📦 Encontrado: {objeto}"
                )



        else:

            print(
                "❌ Edificio no encontrado"
            )



    # -------------------------
    # Revisar amenazas
    # -------------------------


    def revisar_peligros(
        self
    ):


        if self.zona_actual is None:

            return



        cantidad = len(
            self.zona_actual.zombies
        )


        if cantidad > 0:

            print(
                f"⚠️ Hay {cantidad} zombies en la zona"
            )


        else:

            print(
                "✅ Zona segura"
            )