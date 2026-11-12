# 🧟 SupervivenciaGame
# Prueba Sistema Ciclo Día/Noche
# FASE 2.4 - Supervivencia avanzada
# Versión v0.2.4


import sys
import os


# Agregar carpeta scripts al sistema

ruta_scripts = os.path.dirname(
    os.path.abspath(__file__)
)

if ruta_scripts not in sys.path:
    sys.path.insert(
        0,
        ruta_scripts
    )


from day_cycle import CicloDia



print("=" * 60)
print("🌞🌙 PRUEBA CICLO DÍA/NOCHE")
print("=" * 60)



# Crear ciclo del mundo

print("\n🌎 Creando mundo...\n")


tiempo = CicloDia()



# Estado inicial

print("📅 Estado inicial:")

tiempo.mostrar()



# Avanzar 6 horas

print("\n⏳ Avanzan 6 horas...\n")


tiempo.avanzar_tiempo(
    6
)


tiempo.mostrar()



# Avanzar 6 horas

print("\n⏳ Avanzan 6 horas más...\n")


tiempo.avanzar_tiempo(
    6
)


tiempo.mostrar()



# Avanzar 8 horas

print("\n⏳ Avanzan 8 horas...\n")


tiempo.avanzar_tiempo(
    8
)


tiempo.mostrar()



# Avanzar hasta otro día

print("\n⏳ Avanzan 12 horas...\n")


tiempo.avanzar_tiempo(
    12
)


tiempo.mostrar()



# Resultado final

print("\n" + "=" * 60)
print("✅ PRUEBA CICLO DÍA/NOCHE COMPLETADA")
print("=" * 60)