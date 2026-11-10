# 🧟 SupervivenciaGame
# Sistema del Jugador
# Versión: v0.1.1

class Jugador:

    def __init__(self, nombre):

        # Datos principales
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

        # Estados de supervivencia
        self.vida = 100
        self.energia = 100
        self.hambre = 100
        self.sed = 100

        # Posición inicial
        self.posicion = {
            "x": 0,
            "y": 0
        }

        # Inventario inicial
        self.inventario = []

        # Estado actual
        self.estado = "Normal"


    def mostrar_estado(self):

        print("=" * 40)
        print("🧍 ESTADO DEL JUGADOR")
        print("=" * 40)

        print(f"Nombre: {self.nombre}")
        print(f"Nivel: {self.nivel}")
        print(f"Experiencia: {self.experiencia}")

        print("\n❤️ Vida:", self.vida)
        print("⚡ Energía:", self.energia)
        print("🍖 Hambre:", self.hambre)
        print("💧 Sed:", self.sed)

        print("\n📍 Posición:")
        print(self.posicion)

        print("\n🎒 Inventario:")
        if len(self.inventario) == 0:
            print("Vacío")
        else:
            for objeto in self.inventario:
                print("-", objeto)

        print("\nEstado:", self.estado)


    def mover(self, x, y):

        self.posicion["x"] += x
        self.posicion["y"] += y

        self.gastar_energia(5)

        print(
            f"🚶 {self.nombre} se movió "
            f"a ({self.posicion['x']}, {self.posicion['y']})"
        )


    def gastar_energia(self, cantidad):

        self.energia -= cantidad

        if self.energia < 0:
            self.energia = 0

        if self.energia == 0:
            self.estado = "Agotado"


    def recibir_daño(self, daño):

        self.vida -= daño

        if self.vida < 0:
            self.vida = 0

        print(f"💥 Daño recibido: {daño}")

        if self.vida == 0:
            self.estado = "Derrotado"


    def curarse(self, cantidad):

        self.vida += cantidad

        if self.vida > 100:
            self.vida = 100

        print(f"❤️ Curación: +{cantidad}")


    def comer(self, cantidad):

        self.hambre += cantidad

        if self.hambre > 100:
            self.hambre = 100

        print("🍖 El jugador comió")


    def beber(self, cantidad):

        self.sed += cantidad

        if self.sed > 100:
            self.sed = 100

        print("💧 El jugador bebió")


    def agregar_objeto(self, objeto):

        self.inventario.append(objeto)

        print(
            f"🎒 Objeto agregado: {objeto}"
        )


    def ganar_experiencia(self, cantidad):

        self.experiencia += cantidad

        print(
            f"⭐ Experiencia obtenida: {cantidad}"
        )


        if self.experiencia >= 100:

            self.subir_nivel()


    def subir_nivel(self):

        self.nivel += 1
        self.experiencia = 0

        print(
            f"⬆️ Nuevo nivel alcanzado: {self.nivel}"
        )