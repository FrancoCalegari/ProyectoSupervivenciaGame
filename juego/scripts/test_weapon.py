from zombie import Zombie
from weapon import Rifle, Escopeta


zombie = Zombie()

rifle = Rifle()

rifle.mostrar_estado()

rifle.disparar(zombie)

rifle.mostrar_estado()


escopeta = Escopeta()

escopeta.mostrar_estado()

escopeta.disparar(zombie)

zombie.mostrar_estado()