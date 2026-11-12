# 🧟 SupervivenciaGame
# Prueba Mundo + Edificios + Vehículos + Loot
# FASE 2.3 - Mundo vivo
# Versión v0.2.3


import sys
import os


ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

if ruta_scripts not in sys.path:
    sys.path.insert(
        0,
        ruta_scripts
    )


from player import Jugador
from building import Edificio
from container import Contenedor
from vehicle import Vehiculo
from item import Item



print("=" * 70)
print("🌎 PRUEBA MUNDO VIVO COMPLETO")
print("=" * 70)



# -------------------------
# Crear jugador
# -------------------------

print("\n🧍 Creando superviviente...\n")


jugador = Jugador(
    "Superviviente"
)



# -------------------------
# Crear casa
# -------------------------

print("\n🏠 Creando zona residencial...\n")


casa = Edificio(

    "Casa abandonada",

    "Vivienda"

)


casa.agregar_habitacion(
    "Dormitorio"
)

casa.agregar_habitacion(
    "Cocina"
)

casa.agregar_habitacion(
    "Garaje"
)



# -------------------------
# Crear loot casa
# -------------------------

comida = Item(

    "Comida enlatada",

    "Consumible",

    1,

    3,

    "Común",

    True

)


medicamento = Item(

    "Medicamento",

    "Curación",

    1,

    1,

    "Raro",

    False

)



armario = Contenedor(

    "Armario del dormitorio",

    "Armario"

)


armario.agregar_objeto(
    comida
)


armario.agregar_objeto(
    medicamento
)



casa.agregar_contenedor(
    armario
)



# -------------------------
# Explorar casa
# -------------------------

print("\n🔎 Explorando casa...\n")


casa.explorar()


casa.abrir_contenedores()



# Recoger loot

print("\n🎒 Recogiendo recursos...\n")


objetos = armario.saquear_todo()


for objeto in objetos:

    jugador.recibir_item(
        objeto
    )



# -------------------------
# Crear vehículo
# -------------------------

print("\n🚗 Encontrando vehículo abandonado...\n")


auto = Vehiculo(

    "Camioneta vieja",

    "Pickup"

)



herramientas = Item(

    "Herramientas",

    "Herramienta",

    3,

    1,

    "Poco común",

    False

)



auto.agregar_objeto(
    herramientas
)



auto.revisar()


auto.abrir_maletero()



# Reparar vehículo

print("\n🔧 Reparando vehículo...\n")


auto.reparar_motor()


auto.cargar_combustible(
    40
)


auto.encender()



# -------------------------
# Estado final
# -------------------------

print("\n📊 Estado final superviviente:\n")


jugador.mostrar_estado()



print("\n" + "=" * 70)
print("✅ PRUEBA MUNDO VIVO COMPLETADA")
print("=" * 70)