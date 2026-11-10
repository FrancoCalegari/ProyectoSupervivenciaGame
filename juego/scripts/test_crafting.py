# 🧟 SupervivenciaGame
# Prueba de Crafting


from inventory import Inventario, Objeto
from crafting import SistemaCrafting



inventario = Inventario(
    capacidad=20
)



inventario.agregar_objeto(
    Objeto(
        "Tela",
        "Material",
        1,
        5
    )
)



inventario.agregar_objeto(
    Objeto(
        "Alcohol",
        "Material",
        1,
        3
    )
)



inventario.agregar_objeto(
    Objeto(
        "Botella",
        "Material",
        1,
        1
    )
)



crafting = SistemaCrafting(
    inventario
)



crafting.mostrar_recetas()



print("\n🩹 Fabricando venda...\n")


crafting.fabricar(
    "Venda"
)



inventario.mostrar_inventario()