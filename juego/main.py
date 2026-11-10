# 🧟 SupervivenciaGame
# Núcleo principal del juego
# Versión: v0.1.1

import os
import datetime


class SupervivenciaGame:

    def __init__(self):
        self.nombre = "SupervivenciaGame"
        self.version = "v0.1.1"
        self.estado = "Inicializando"
        self.fecha_inicio = datetime.datetime.now()

    def iniciar(self):
        self.estado = "Activo"

        print("=" * 50)
        print("🧟 SUPERVIVIENCIAGAME")
        print("=" * 50)

        print(f"🎮 Juego: {self.nombre}")
        print(f"📌 Versión: {self.version}")
        print(f"⚙️ Estado: {self.estado}")

        print("\n🌎 Mundo postapocalíptico cargado")
        print("🧍 Sistema de jugador preparado")
        print("🧟 Sistema de amenazas preparado")
        print("🎒 Inventario inicial preparado")
        print("💾 Sistema base iniciado")

        print("\n🚀 SupervivenciaGame iniciado correctamente")


    def cerrar(self):
        self.estado = "Cerrado"

        print("\n🛑 Cerrando juego...")
        print("💾 Guardando información...")
        print("✅ Juego cerrado correctamente")


def main():

    juego = SupervivenciaGame()

    try:
        juego.iniciar()

    except Exception as error:
        print("❌ Error:", error)

    finally:
        juego.cerrar()


if __name__ == "__main__":
    main()