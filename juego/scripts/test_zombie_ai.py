# 🧟 SupervivenciaGame
# Prueba del Sistema de IA de Zombies
# Versión: v0.1.1


from player import Jugador
from zombie import Zombie
from zombie_ai import ZombieIA



# Crear jugador

jugador = Jugador(
    "Superviviente"
)


# Colocar jugador cerca del zombie

jugador.posicion = {
    "x": 5,
    "y": 5
}



# Crear zombie

zombie = Zombie()


zombie.posicion = {
    "x": 10,
    "y": 10
}



# Crear inteligencia artificial

ia = ZombieIA(
    zombie
)



print("=" * 50)
print("🤖 PRUEBA DE IA DE ZOMBIE")
print("=" * 50)



# Mostrar estados iniciales

jugador.mostrar_estado()

zombie.mostrar_estado()



print("\n👁️ PRUEBA DE DETECCIÓN")

ia.detectar_jugador(
    jugador
)



print("\n🔄 ACTUALIZANDO IA")

ia.actualizar()



print("\n👂 PRUEBA DE RUIDO")

ia.escuchar_ruido(
    {
        "x": 7,
        "y": 7
    }
)



ia.actualizar()



print("\n⚔️ PRUEBA DE COMBATE")

ia.detectar_jugador(
    jugador
)


for i in range(3):

    print(
        f"\nTurno IA {i + 1}"
    )

    ia.actualizar()



print("\n✅ PRUEBA FINALIZADA")