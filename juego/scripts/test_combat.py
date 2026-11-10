from player import Jugador
from zombie import Zombie
from weapon import Rifle
from combat import Combate


jugador = Jugador("Superviviente")

zombie = Zombie()

rifle = Rifle()


combate = Combate(jugador)


combate.iniciar_combate(
    zombie
)


combate.atacar_con_arma(
    rifle
)


combate.recibir_ataque()


combate.mostrar_estadisticas()