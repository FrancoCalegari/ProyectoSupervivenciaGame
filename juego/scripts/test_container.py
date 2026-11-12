# 🧟 SupervivenciaGame
# Prueba Sistema de Contenedores y Loot
# FASE 2.2 - Mundo con exploración real
# Versión v0.2.2


import sys
import os


# Agregar carpeta scripts

ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

sys.path.append(
    ruta_scripts
)


from container import Contenedor
from item import Item



print("=" * 60)
print("📦 PRUEBA SISTEMA DE CONTENEDORES")
print("=" * 60)



# Crear objetos para loot

print("\n📦 Creando objetos disponibles...\n")


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



municion = Item(

    nombre="Munición",

    tipo="Munición",

    peso=1,

    cantidad=15,

    rareza="Común",

    apilable=True

)



lista_loot = [

    madera,

    comida,

    medicamento,

    municion

]



# Crear contenedor

print("\n🏠 Creando casa abandonada...\n")


armario = Contenedor(

    nombre="Armario viejo",

    tipo="Armario"

)



# Generar loot

armario.generar_loot(
    lista_loot
)



# Mostrar contenido cerrado

print("\n📦 Estado inicial:\n")

armario.mostrar()



# Abrir

print("\n🔓 Abriendo contenedor...\n")


armario.abrir()



# Mostrar contenido

print("\n📊 Contenido encontrado:\n")


armario.mostrar()



# Sacar objeto

print("\n🎒 Sacando comida...\n")


objeto = armario.sacar_objeto(
    "Comida enlatada"
)



if objeto:

    print(
        f"✅ Obtenido: {objeto.nombre}"
    )



# Mostrar después del saqueo

print("\n📦 Después de recoger objeto:\n")


armario.mostrar()



# Saquear todo

print("\n🎒 Saqueando todo...\n")


objetos = armario.saquear_todo()



for item in objetos:

    print(
        f"Obtenido: {item.nombre} x{item.cantidad}"
    )



# Estado final

print("\n📦 Estado final del contenedor:\n")


armario.mostrar()



print("\n" + "=" * 60)
print("✅ PRUEBA CONTENEDORES COMPLETADA")
print("=" * 60)