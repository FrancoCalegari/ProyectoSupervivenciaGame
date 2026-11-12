# 🧟 SupervivenciaGame
# Prueba Sistema de Movimiento del Jugador
# FASE 2 - Mundo Jugable
# Versión v0.2.0


import sys
import os


# Agregar carpeta scripts al buscador de Python

ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

sys.path.append(
    ruta_scripts
)


from player import Jugador



print("=" * 60)
print("🚶 PRUEBA SISTEMA DE MOVIMIENTO")
print("=" * 60)



# Crear jugador

jugador = Jugador(
    "Superviviente"
)



print("\n📊 ESTADO INICIAL\n")

jugador.mostrar_estado()



# Movimiento por el mapa

print("\n🚶 MOVIMIENTOS\n")


jugador.mover(
    "norte"
)


jugador.mover(
    "norte"
)


jugador.mover(
    "este"
)


jugador.mover(
    "este"
)


jugador.mover(
    "sur"
)


jugador.mover(
    "oeste"
)



print("\n📍 CAMBIANDO ZONA\n")


jugador.cambiar_zona(
    "Bosque"
)



print("\n💥 RECIBIENDO DAÑO\n")


jugador.recibir_danio(
    25
)



print("\n❤️ CURANDO JUGADOR\n")


jugador.curar(
    15
)



print("\n😴 DESCANSANDO\n")


jugador.descansar()



print("\n📊 ESTADO FINAL\n")


jugador.mostrar_estado()



print("\n" + "=" * 60)
print("✅ PRUEBA DE MOVIMIENTO COMPLETADA")
print("=" * 60)