# 🧟 SupervivenciaGame
# Prueba Sistema de Spawn de Zombies
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
from spawn import SistemaSpawn



print("=" * 60)
print("🧟 PRUEBA SISTEMA DE SPAWN")
print("=" * 60)



# Crear mundo

print("\n🌎 Creando mundo...\n")


mundo = Mundo(
    "Zona Cero"
)



mundo.iniciar_mundo()



# Crear sistema spawn

print("\n🧟 Activando sistema de aparición...\n")


spawn = SistemaSpawn(
    mundo
)



# Generar amenazas iniciales

spawn.generar_mundo_inicial()



# Mostrar todos los zombies

print("\n📊 ESTADO DE AMENAZAS\n")


spawn.mostrar_zombies()



# Mostrar zonas con zombies

print("\n📍 REVISANDO ZONAS\n")


for zona in mundo.mapa.localizaciones:

    print("=" * 50)

    print(
        f"📍 Zona: {zona.nombre}"
    )

    print(
        f"🧟 Zombies: {len(zona.zombies)}"
    )


    for zombie in zona.zombies:

        print(
            f"- {zombie['tipo']} "
            f"(Vida: {zombie['vida']} "
            f"Daño: {zombie['daño']})"
        )



print("\n" + "=" * 60)
print("✅ PRUEBA DE SPAWN COMPLETADA")
print("=" * 60)