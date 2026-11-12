# 🧟 SupervivenciaGame
# Prueba Contenedor + Jugador + Inventario
# FASE 2.2 - Loot conectado
# Versión v0.2.2


import sys
import os


# Agregar carpeta scripts

ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

if ruta_scripts not in sys.path:

    sys.path.insert(
        0,
        ruta_scripts
    )


from player import Jugador
from container import Contenedor
from item import Item



print("=" * 60)
print("📦 PRUEBA LOOT + JUGADOR + INVENTARIO")
print("=" * 60)



# Crear jugador

print("\n🧍 Creando superviviente...\n")


jugador = Jugador(
    "Superviviente"
)



# Crear objetos dentro del contenedor

print("\n🎁 Creando loot...\n")


madera = Item(

    nombre="Madera",

    tipo="Recurso",

    peso=2,

    cantidad=5,

    rareza="Común",

    apilable=True

)



comida = Item(

    nombre="Comida enlatada",

    tipo="Consumible",

    peso=1,

    cantidad=2,

    rareza="Poco común",

    apilable=True

)



medicamento = Item(

    nombre="Medicamento",

    tipo="Curación",

    peso=1,

    cantidad=1,

    rareza="Raro",

    apilable=False

)



# Crear contenedor

print("\n🏠 Creando casa abandonada...\n")


armario = Contenedor(

    nombre="Armario de casa abandonada",

    tipo="Armario"

)



# Agregar objetos al contenedor

armario.agregar_objeto(
    madera
)

armario.agregar_objeto(
    comida
)

armario.agregar_objeto(
    medicamento
)



# Abrir contenedor

print("\n🔓 Abriendo armario...\n")


armario.abrir()



# Mostrar contenido

print("\n📦 Contenido encontrado:\n")


armario.mostrar()



# Transferir loot al jugador

print("\n🎒 Recogiendo objetos...\n")


objetos = armario.saquear_todo()



for objeto in objetos:


    jugador.recibir_item(
        objeto
    )



# Mostrar estado jugador

print("\n📊 Estado final del jugador:\n")


jugador.mostrar_estado()



# Mostrar contenedor vacío

print("\n📦 Estado del contenedor:\n")


armario.mostrar()



print("\n" + "=" * 60)
print("✅ PRUEBA LOOT + JUGADOR COMPLETADA")
print("=" * 60)