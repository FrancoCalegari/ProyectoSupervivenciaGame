# 🧟 SupervivenciaGame
# Prueba Sistema de Interacción con el Mundo
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


from world import Mundo
from player import Jugador
from interaction import SistemaInteraccion



print("=" * 60)
print("🎒 PRUEBA SISTEMA DE INTERACCIÓN")
print("=" * 60)



# Crear mundo

print("\n🌎 Creando mundo...\n")


mundo = Mundo(
    "Zona Cero"
)


mundo.iniciar_mundo()



# Crear jugador

print("\n🧍 Creando jugador...\n")


jugador = Jugador(
    "Superviviente"
)



mundo.colocar_jugador(
    jugador
)



# Crear sistema de interacción

print("\n🎒 Activando sistema de interacción...\n")


interaccion = SistemaInteraccion(
    jugador,
    mundo
)



# Entrar en casa abandonada

print("\n🏚️ Explorando casa abandonada\n")


interaccion.cambiar_zona(
    "Casa abandonada"
)



# Revisar zona

print("\n🔎 Revisando zona\n")


interaccion.revisar_zona()



# Recoger recursos

print("\n🎒 Recogiendo recursos\n")


interaccion.recoger_recurso(
    "Comida"
)


interaccion.recoger_recurso(
    "Tela"
)



# Entrar edificio

print("\n🏠 Entrando edificio\n")


interaccion.entrar_edificio(
    "Casa pequeña"
)



# Revisar peligros

print("\n⚠️ Revisando amenazas\n")


interaccion.revisar_peligros()



# Cambiar a ciudad

print("\n🏙️ Viajando a ciudad abandonada\n")


interaccion.cambiar_zona(
    "Ciudad abandonada"
)



interaccion.revisar_zona()



# Estado final jugador

print("\n📊 Estado final del jugador\n")


jugador.mostrar_estado()



print("\n" + "=" * 60)
print("✅ PRUEBA DE INTERACCIÓN COMPLETADA")
print("=" * 60)