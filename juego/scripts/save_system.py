# 🧟 SupervivenciaGame
# Sistema de Guardado de Partidas
# FASE 2 - Mundo Jugable
# Versión v0.2.0


import json
import os



class SistemaGuardado:


    def __init__(
        self,
        carpeta="saves"
    ):

        self.carpeta = carpeta


        if not os.path.exists(
            self.carpeta
        ):

            os.makedirs(
                self.carpeta
            )



    # -------------------------
    # Crear datos de guardado
    # -------------------------


    def crear_datos(
        self,
        jugador,
        mundo
    ):


        datos = {


            "jugador": {

                "nombre": jugador.nombre,

                "vida": jugador.vida,

                "energia": jugador.energia,

                "hambre": jugador.hambre,

                "sed": jugador.sed,

                "nivel": jugador.nivel,

                "experiencia": jugador.experiencia,

                "posicion": jugador.posicion,

                "zona_actual": jugador.zona_actual

            },


            "mundo": {

                "nombre": mundo.nombre,

                "dia": mundo.dia,

                "hora": mundo.hora,

                "clima": mundo.clima,

                "zombies": len(mundo.zombies)

            }

        }


        return datos



    # -------------------------
    # Guardar partida
    # -------------------------


    def guardar(
        self,
        slot,
        jugador,
        mundo
    ):


        datos = self.crear_datos(
            jugador,
            mundo
        )


        archivo = os.path.join(

            self.carpeta,

            f"slot_{slot}.json"

        )


        with open(
            archivo,
            "w",
            encoding="utf-8"
        ) as archivo_json:


            json.dump(

                datos,

                archivo_json,

                indent=4,

                ensure_ascii=False

            )


        print(
            f"💾 Partida guardada en slot {slot}"
        )



    # -------------------------
    # Cargar partida
    # -------------------------


    def cargar(
        self,
        slot
    ):


        archivo = os.path.join(

            self.carpeta,

            f"slot_{slot}.json"

        )


        if not os.path.exists(
            archivo
        ):

            print(
                "❌ No existe esa partida"
            )

            return None



        with open(

            archivo,

            "r",

            encoding="utf-8"

        ) as archivo_json:


            datos = json.load(
                archivo_json
            )


        print(
            f"📂 Partida cargada desde slot {slot}"
        )


        return datos



    # -------------------------
    # Mostrar slots
    # -------------------------


    def mostrar_slots(
        self
    ):


        print("=" * 50)

        print(
            "💾 PARTIDAS GUARDADAS"
        )

        print("=" * 50)



        encontrados = False


        for archivo in os.listdir(
            self.carpeta
        ):


            if archivo.endswith(
                ".json"
            ):


                encontrados = True


                ruta = os.path.join(

                    self.carpeta,

                    archivo

                )


                with open(

                    ruta,

                    "r",

                    encoding="utf-8"

                ) as f:


                    datos = json.load(
                        f
                    )


                jugador = datos["jugador"]["nombre"]

                dia = datos["mundo"]["dia"]


                print(
                    f"📁 {archivo} | "
                    f"Jugador: {jugador} | "
                    f"Día: {dia}"
                )



        if not encontrados:

            print(
                "No hay partidas guardadas"
            )



    # -------------------------
    # Eliminar partida
    # -------------------------


    def eliminar(
        self,
        slot
    ):


        archivo = os.path.join(

            self.carpeta,

            f"slot_{slot}.json"

        )


        if os.path.exists(
            archivo
        ):


            os.remove(
                archivo
            )


            print(
                f"🗑️ Slot {slot} eliminado"
            )


        else:

            print(
                "❌ No existe ese slot"
            )