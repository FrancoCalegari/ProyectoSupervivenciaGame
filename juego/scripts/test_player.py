from player import Jugador


jugador = Jugador("Superviviente")

jugador.mostrar_estado()

jugador.mover(5, 3)

jugador.agregar_objeto("Cuchillo")

jugador.ganar_experiencia(100)

jugador.mostrar_estado()