# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solis
# Fecha: 28/09/2026    Versión: 1.0
# Descripción: Verifica si una nave posee suficiente combustible
#              para la misión y advierte si el margen es bajo.
# ============================================================

# ------------------------------------------------------------
# Declaración de constantes
# ------------------------------------------------------------
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO_ADICIONAL = 10

# ------------------------------------------------------------
# Entrada de datos
# ------------------------------------------------------------
combustible_disponible = int(input("Combustible disponible (unidades): "))
combustible_ida = int(input("Combustible requerido para llegar al destino (unidades): "))
combustible_regreso = int(input("Combustible requerido para regresar (unidades): "))

# ------------------------------------------------------------
# Procesamiento
# La reserva se suma una sola vez porque cubre emergencias de toda la misión.
# ------------------------------------------------------------
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total_requerido

# ------------------------------------------------------------
# Salida de resultados
# Estos seis datos se muestran siempre, sin importar el margen.
# ------------------------------------------------------------
print()
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional disponible:", combustible_adicional, "unidades")

# ------------------------------------------------------------
# Decisión
# Se usa < y no <= porque un margen de exactamente 10 unidades
# todavía se considera aceptable. Sin else: solo se advierte en este caso.
# ------------------------------------------------------------
if combustible_adicional < MARGEN_MINIMO_ADICIONAL:
    print("Advertencia: el margen adicional de combustible es bajo.")