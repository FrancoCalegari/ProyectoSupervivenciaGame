# 🧟 SupervivenciaGame
# Prueba Sistema de Guardado
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
from save_system import SistemaGuardado



print("=" * 60)
print("💾 PRUEBA SISTEMA DE GUARDADO")
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



# Cambiar datos para probar guardado

jugador.mover(
    "norte"
)


jugador.mover(
    "este"
)


jugador.cambiar_zona(
    "Bosque"
)



mundo.dia = 2

mundo.hora = 15

mundo.clima = "Lluvia"



# Crear sistema de guardado

print("\n💾 Activando sistema de guardado...\n")


guardado = SistemaGuardado()



# Guardar partida

print("\n💾 Guardando partida...\n")


guardado.guardar(
    1,
    jugador,
    mundo
)



# Mostrar slots

print("\n📁 Slots disponibles...\n")


guardado.mostrar_slots()



# Cargar partida

print("\n📂 Cargando partida...\n")


partida = guardado.cargar(
    1
)



print("\n📊 DATOS RECUPERADOS\n")


print("=" * 50)


print(
    "🧍 Jugador:"
)

print(
    partida["jugador"]
)



print(
    "\n🌎 Mundo:"
)

print(
    partida["mundo"]
)



print("=" * 50)



# Probar eliminación

print("\n🗑️ Eliminando slot de prueba...\n")


guardado.eliminar(
    1
)



print("\n📁 Slots después de eliminar:\n")


guardado.mostrar_slots()



print("\n" + "=" * 60)
print("✅ PRUEBA DE GUARDADO COMPLETADA")
print("=" * 60)