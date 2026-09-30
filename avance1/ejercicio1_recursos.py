# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solis
# Fecha: 30/09/2026    Versión: 1.1
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
TRAMOS_VIAJE = 2

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

# Oxígeno, energía y provisiones cubren ida y regreso, por eso el consumo
# diario se multiplica por TRAMOS_VIAJE. Las cantidades fijas (emergencia,exploración y adicionales) se suman una sola vez.
oxigeno_requerido = dias_viaje * CONSUMO_OXIGENO_DIARIO * TRAMOS_VIAJE * cantidad_tripulantes + OXIGENO_EMERGENCIA
energia_requerida = dias_viaje * CONSUMO_ENERGIA_DIARIO * TRAMOS_VIAJE + ENERGIA_EXPLORACION
provisiones_requeridas = dias_viaje * cantidad_tripulantes * CONSUMO_PROVISIONES_DIARIO * TRAMOS_VIAJE + PROVISIONES_ADICIONALES

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