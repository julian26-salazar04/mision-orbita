# ============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solís
# Fecha: 21/10/2026    Versión: 1.0
# Descripción: Evalúa si la nave puede regresar a la Tierra (caso A)
#              o si la tripulación queda varada (caso B).
# ============================================================

# --- Declaración de constantes ---
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# --- Entrada de datos ---
tripulantes = int(input("Cantidad de tripulantes: "))
dias_ida = int(input("Cantidad de días del viaje de ida: "))
combustible = int(input("Combustible disponible: "))
oxigeno = int(input("Oxígeno disponible: "))
energia = int(input("Energía disponible: "))
provisiones = int(input("Provisiones disponibles: "))

# --- Procesamiento inicial ---
# La reserva de emergencia no se suma en este ejercicio.
combustible_regreso = dias_ida * CONSUMO_COMBUSTIBLE_DIA
consumo_oxigeno_dia = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
consumo_provisiones_dia = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

print("")

# --- Decisión: caso A (regreso) o caso B (varada) ---
if combustible >= combustible_regreso:
    # --- Caso A: simulación del regreso día a día ---
    dias_completados = 0
    puede_continuar = True

    # El ciclo termina al completar los días o al faltar algún recurso.
    while dias_completados < dias_ida and puede_continuar:
        # Se verifica antes de consumir; si falta algo, el día no se descuenta.
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno >= consumo_oxigeno_dia
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= consumo_provisiones_dia):
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - consumo_oxigeno_dia
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - consumo_provisiones_dia
            dias_completados = dias_completados + 1
            print("Día", dias_completados, "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno, "| Energía:", energia,
                  "| Provisiones:", provisiones)
        else:
            puede_continuar = False

    # --- Salida según cómo terminó el ciclo ---
    if dias_completados == dias_ida:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        dia_interrumpido = dias_completados + 1
        print("El regreso se interrumpió en el día", str(dia_interrumpido) + ".")
        # El combustible nunca falta aquí: ya se verificó en la decisión inicial.
        if oxigeno < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
else:
    # --- Caso B: tripulación varada ---
    print("La tripulación quedó varada en el destino.")

    dias_oxigeno = oxigeno // consumo_oxigeno_dia
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // consumo_provisiones_dia

    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)

    # Menor de los tres valores, sin usar min().
    supervivencia = dias_oxigeno
    if dias_energia < supervivencia:
        supervivencia = dias_energia
    if dias_provisiones < supervivencia:
        supervivencia = dias_provisiones

    # Se listan todos los recursos empatados en el mínimo, separados por coma.
    limitantes = ""
    if dias_oxigeno == supervivencia:
        limitantes = "oxígeno"
    if dias_energia == supervivencia:
        if limitantes == "":
            limitantes = "energía"
        else:
            limitantes = limitantes + ", energía"
    if dias_provisiones == supervivencia:
        if limitantes == "":
            limitantes = "provisiones"
        else:
            limitantes = limitantes + ", provisiones"

    print("Supervivencia estimada:", supervivencia, "días")
    print("Recurso(s) limitante(s):", limitantes)