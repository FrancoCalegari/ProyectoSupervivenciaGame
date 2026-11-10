from player import Jugador
from zombie import Zombie


jugador = Jugador("Superviviente")


zombie = Zombie()

zombie.mostrar_estado()

zombie.detectar_jugador(jugador)

zombie.perseguir()

zombie.atacar()

zombie.recibir_daño(100)

zombie.mostrar_estado()