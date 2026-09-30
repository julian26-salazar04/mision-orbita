# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solis
# Fecha: 29/09/2026    Versión: 1.0
# Descripción: Verifica si la nave posee oxígeno y provisiones
#              suficientes para mantener a la tripulación.
# ============================================================

# ------------------------------------------------------------
# Entrada de datos
# ------------------------------------------------------------
oxigeno_disponible = int(input("Oxígeno disponible (unidades): "))
oxigeno_requerido = int(input("Oxígeno requerido (unidades): "))
provisiones_disponibles = int(input("Provisiones disponibles (unidades): "))
provisiones_requeridas = int(input("Provisiones requeridas (unidades): "))

# ------------------------------------------------------------
# Decisión y salida de resultados
# Se usa and porque la tripulación solo tiene soporte adecuado si
# ambos recursos alcanzan; con >= se acepta el caso exacto del mínimo.
# Todavía no se indica cuál recurso falla, según la consigna.
# ------------------------------------------------------------
print()
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")