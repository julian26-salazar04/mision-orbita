# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solis
# Fecha: 28/09/2026    Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión.
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes
# Se definen aquí para evitar números mágicos en las fórmulas.
# ------------------------------------------------------------
CONSUMO_COMBUSTIBLE_DIARIO = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_DIARIO = 2
OXIGENO_EMERGENCIA = 5
CONSUMO_ENERGIA_DIARIO = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES_DIARIO = 1
PROVISIONES_ADICIONALES = 3

# ------------------------------------------------------------
# Entrada de datos
# ------------------------------------------------------------
nombre_mision = input("Nombre de la misión: ")
cantidad_tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días estimados para llegar al destino: "))

# ------------------------------------------------------------
# Procesamiento
# El regreso dura lo mismo que la ida, por eso usa los mismos días.
# La reserva se suma una sola vez al total, para emergencias.
# ------------------------------------------------------------
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# Oxígeno, energía y provisiones se consumen solo en el viaje de ida.
oxigeno_requerido = dias_viaje * cantidad_tripulantes * CONSUMO_OXIGENO_DIARIO + OXIGENO_EMERGENCIA
energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIARIO + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * cantidad_tripulantes * CONSUMO_PROVISIONES_DIARIO + PROVISIONES_ADICIONALES

# ------------------------------------------------------------
# Salida de resultados
# ------------------------------------------------------------
print()
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")