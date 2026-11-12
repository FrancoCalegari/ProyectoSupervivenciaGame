# 🧟 SupervivenciaGame
# Prueba del Sistema de Recursos
# Versión v0.1.1


from inventory import Inventario
from resources import SistemaRecursos


inventario = Inventario(
    capacidad=20
)


recursos = SistemaRecursos(
    inventario
)


print("=" * 45)
print("🌲 PRUEBA SISTEMA DE RECURSOS")
print("=" * 45)


recursos.mostrar_recursos()


print("\n🌲 Recolectando madera...\n")

recursos.recolectar_recurso(
    "Árbol",
    3
)


print("\n⛏️ Recolectando metal...\n")

recursos.recolectar_recurso(
    "Chatarra",
    2
)


print("\n🎒 Inventario final\n")

inventario.mostrar_inventario()


print("\n♻️ Restaurando recursos\n")

recursos.restaurar_todos()


print("\n✅ Prueba terminada")