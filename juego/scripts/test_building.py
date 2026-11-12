# 🧟 SupervivenciaGame
# Prueba Sistema de Edificios Explorables
# FASE 2.3 - Mundo vivo
# Versión v0.2.3


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


from building import Edificio
from container import Contenedor
from item import Item



print("=" * 60)
print("🏠 PRUEBA SISTEMA DE EDIFICIOS")
print("=" * 60)



# Crear edificio

print("\n🏠 Creando casa abandonada...\n")


casa = Edificio(

    nombre="Casa abandonada",

    tipo="Vivienda"

)



# Crear habitaciones

casa.agregar_habitacion(
    "Dormitorio"
)

casa.agregar_habitacion(
    "Cocina"
)

casa.agregar_habitacion(
    "Garaje"
)



# Crear objetos

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

    cantidad=3,

    rareza="Común",

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



# Crear contenedores

print("\n📦 Creando contenedores...\n")


armario = Contenedor(

    nombre="Armario del dormitorio",

    tipo="Armario"

)


caja = Contenedor(

    nombre="Caja de herramientas",

    tipo="Caja"

)



# Agregar loot

armario.agregar_objeto(
    comida
)

armario.agregar_objeto(
    medicamento
)


caja.agregar_objeto(
    madera
)



# Añadir contenedores a la casa

casa.agregar_contenedor(
    armario
)


casa.agregar_contenedor(
    caja
)



# Mostrar edificio

print("\n📊 Información inicial:\n")

casa.mostrar()



# Explorar

print("\n🔎 Explorando edificio...\n")

casa.explorar()



# Revisar contenedores

print("\n📦 Revisando loot...\n")

casa.abrir_contenedores()



# Mostrar estado final

print("\n📊 Estado final:\n")

casa.mostrar()



print("\n" + "=" * 60)
print("✅ PRUEBA EDIFICIOS COMPLETADA")
print("=" * 60)