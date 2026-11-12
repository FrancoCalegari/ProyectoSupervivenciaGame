# 🧟 SupervivenciaGame
# Prueba Sistema de Vehículos
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


from vehicle import Vehiculo
from item import Item



print("=" * 60)
print("🚗 PRUEBA SISTEMA DE VEHÍCULOS")
print("=" * 60)



# Crear vehículo

print("\n🚗 Encontrando vehículo abandonado...\n")


auto = Vehiculo(

    nombre="Sedán abandonado",

    tipo="Auto"

)



# Crear objetos del maletero

print("\n📦 Preparando maletero...\n")


herramientas = Item(

    nombre="Herramientas",

    tipo="Herramienta",

    peso=3,

    cantidad=1,

    rareza="Poco común",

    apilable=False

)



combustible = Item(

    nombre="Bidón de gasolina",

    tipo="Combustible",

    peso=5,

    cantidad=1,

    rareza="Raro",

    apilable=False

)



comida = Item(

    nombre="Comida enlatada",

    tipo="Consumible",

    peso=1,

    cantidad=2,

    rareza="Común",

    apilable=True

)



# Agregar objetos al maletero

auto.agregar_objeto(
    herramientas
)

auto.agregar_objeto(
    combustible
)

auto.agregar_objeto(
    comida
)



# Estado inicial

print("\n📊 Estado del vehículo:\n")


auto.revisar()



# Abrir maletero

print("\n📦 Abriendo maletero...\n")


auto.abrir_maletero()



# Sacar herramientas

print("\n🎒 Sacando herramientas...\n")


objeto = auto.sacar_objeto(
    "Herramientas"
)



if objeto:

    print(
        f"✅ Conseguido: {objeto.nombre}"
    )



# Reparar motor

print("\n🔧 Reparando vehículo...\n")


auto.reparar_motor()



# Cargar combustible

print("\n⛽ Cargando combustible...\n")


auto.cargar_combustible(
    50
)



# Intentar encender

print("\n🚗 Intentando encender...\n")


auto.encender()



# Estado final

print("\n📊 Estado final del vehículo:\n")


auto.revisar()



print("\n" + "=" * 60)
print("✅ PRUEBA VEHÍCULO COMPLETADA")
print("=" * 60)