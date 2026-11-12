# 🧟 SupervivenciaGame
# Prueba Sistema de Necesidades
# FASE 2.4 - Supervivencia avanzada
# Versión v0.2.4


import sys
import os


# Agregar carpeta scripts

ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

if ruta_scripts not in sys.path:

    sys.path.insert(
        0,
        ruta_scripts
    )


from needs import Necesidades



print("=" * 60)
print("🥩 PRUEBA SISTEMA DE NECESIDADES")
print("=" * 60)



# Crear necesidades del jugador

print("\n🧍 Creando superviviente...\n")


necesidades = Necesidades()



# Estado inicial

print("📊 Estado inicial:\n")


necesidades.mostrar()



# Pasar tiempo

print("\n⏳ Pasan 5 horas de supervivencia...\n")


necesidades.pasar_tiempo(
    5
)



necesidades.mostrar()



# Comer

print("\n🍖 Encontró comida...\n")


necesidades.comer(
    40
)



necesidades.mostrar()



# Beber

print("\n💧 Encontró agua...\n")


necesidades.beber(
    50
)



necesidades.mostrar()



# Cambiar temperatura

print("\n❄️ Entrando en zona fría...\n")


necesidades.cambiar_temperatura(
    -40
)



necesidades.mostrar()



# Dormir

print("\n😴 El superviviente duerme 8 horas...\n")


necesidades.dormir(
    8
)



necesidades.mostrar()



# Prueba de estado crítico

print("\n⚠️ Simulando falta de recursos...\n")


necesidades.pasar_tiempo(
    15
)



necesidades.mostrar()



print("\n" + "=" * 60)
print("✅ PRUEBA NECESIDADES COMPLETADA")
print("=" * 60)