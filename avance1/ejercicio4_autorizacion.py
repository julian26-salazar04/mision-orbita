# ============================================================
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solis
# Fecha: 30/09/2026    Versión: 1.0
# Descripción: Verifica si una misión puede ser autorizada para
#              el lanzamiento según sus recursos disponibles.
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes
# ------------------------------------------------------------
RESERVA_COMBUSTIBLE = 10

# ------------------------------------------------------------
# Entrada de datos
# ------------------------------------------------------------
combustible_disponible = int(input("Combustible disponible (unidades): "))
combustible_ida = int(input("Combustible requerido para llegar al destino (unidades): "))
combustible_regreso = int(input("Combustible requerido para regresar (unidades): "))
oxigeno_disponible = int(input("Oxígeno disponible (unidades): "))
oxigeno_requerido = int(input("Oxígeno requerido (unidades): "))
energia_disponible = int(input("Energía disponible (unidades): "))
energia_requerida = int(input("Energía requerida (unidades): "))
provisiones_disponibles = int(input("Provisiones disponibles (unidades): "))
provisiones_requeridas = int(input("Provisiones requeridas (unidades): "))

# ------------------------------------------------------------
# Procesamiento
# El combustible total incluye el regreso y la reserva, para no
# autorizar misiones que solo pueden llegar al destino.
# ------------------------------------------------------------
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# ------------------------------------------------------------
# Decisión y salida de resultados
# Se usa and porque el lanzamiento solo se autoriza si los cuatro
# recursos alcanzan; >= acepta el caso exacto del mínimo.
# Todavía no se indica cuál recurso provocó el rechazo.
# ------------------------------------------------------------
print()
if (combustible_disponible >= combustible_total_requerido
        and oxigeno_disponible >= oxigeno_requerido
        and energia_disponible >= energia_requerida
        and provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")