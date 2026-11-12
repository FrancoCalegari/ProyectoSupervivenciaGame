# 🧟 SupervivenciaGame
# Prueba Sistema de Exploración
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
from explorer import Explorador



print("=" * 60)
print("🧭 PRUEBA SISTEMA DE EXPLORACIÓN")
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



# Crear explorador

print("\n🧭 Activando explorador...\n")


explorador = Explorador(
    jugador,
    mundo
)



# Iniciar en una zona

print("\n🏚️ Punto inicial\n")


explorador.iniciar_exploracion(
    "Casa abandonada"
)



# Mostrar zona

explorador.mostrar_zona()



# Buscar recursos

print("\n🌲 Buscando recursos\n")


explorador.buscar_recursos()



# Detectar peligros

print("\n⚠️ Revisando peligros\n")


explorador.detectar_peligros()



# Viajar al bosque

print("\n🌲 Viajando al bosque\n")


explorador.viajar(
    "Bosque"
)



explorador.buscar_recursos()



explorador.detectar_peligros()



# Viajar a ciudad

print("\n🏙️ Viajando a ciudad\n")


explorador.viajar(
    "Ciudad abandonada"
)



explorador.mostrar_zona()



# Estado final del jugador

print("\n📊 Estado final del jugador\n")


jugador.mostrar_estado()



print("\n" + "=" * 60)
print("✅ PRUEBA DE EXPLORACIÓN COMPLETADA")
print("=" * 60)