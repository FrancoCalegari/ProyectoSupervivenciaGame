# 🧟 SupervivenciaGame
# Prueba del Inventario


from inventory import Inventario, Objeto



inventario = Inventario(
    capacidad=10
)



agua = Objeto(
    "Botella de agua",
    "Consumible",
    1,
    3
)


municion = Objeto(
    "Munición 9mm",
    "Munición",
    0.1,
    15
)


botiquin = Objeto(
    "Botiquín",
    "Medicina",
    2,
    1
)



inventario.agregar_objeto(
    agua
)


inventario.agregar_objeto(
    municion
)


inventario.agregar_objeto(
    botiquin
)



inventario.mostrar_inventario()



print(
    "\n⚖️ Peso total:",
    inventario.peso_total()
)



inventario.usar_objeto(
    "Botiquín"
)



inventario.quitar_objeto(
    "Munición 9mm",
    5
)



inventario.mostrar_inventario()