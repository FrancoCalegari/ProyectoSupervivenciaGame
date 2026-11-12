# 🧟 SupervivenciaGame
# Prueba del Sistema de Mundo
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
from zombie import Zombie



print("=" * 60)
print("🌎 PRUEBA DEL SISTEMA DE MUNDO")
print("=" * 60)



# Crear mundo

mundo = Mundo(
    "Zona Cero"
)



# Crear mapa y zonas

mundo.iniciar_mundo()



print("\n🧍 CREANDO JUGADOR\n")


jugador = Jugador(
    "Superviviente"
)



mundo.colocar_jugador(
    jugador
)



print("\n🧟 CREANDO ZOMBIES\n")



zombie1 = Zombie()

zombie1.nombre = "Zombie Comun"



zombie2 = Zombie()

zombie2.nombre = "Zombie Corredor"



mundo.agregar_zombie(
    zombie1
)


mundo.agregar_zombie(
    zombie2
)



print("\n📊 ESTADO INICIAL DEL MUNDO\n")


mundo.mostrar_estado()



print("\n📍 EXPLORANDO ZONAS\n")



mundo.entrar_zona(
    "Casa abandonada"
)



mundo.entrar_zona(
    "Bosque"
)



mundo.entrar_zona(
    "Ciudad abandonada"
)



print("\n⏰ AVANZANDO TIEMPO\n")


for i in range(3):

    mundo.cambiar_hora()



print("\n🌧️ CAMBIANDO CLIMA\n")


mundo.cambiar_clima(
    "Tormenta"
)



print("\n📊 ESTADO FINAL DEL MUNDO\n")


mundo.mostrar_estado()



print("\n" + "=" * 60)
print("✅ PRUEBA DEL MUNDO COMPLETADA")
print("=" * 60)