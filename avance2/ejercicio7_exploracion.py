# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Julián Salazar Solís
# Fecha: 21/10/2026    Versión: 1.0
# Descripción: Presenta un menú repetitivo de actividades de
#              exploración científica una vez alcanzado el destino.
# ============================================================

# --- Declaración de constantes ---
OPCION_TERRENO = 1
OPCION_MUESTRA = 2
OPCION_OBSERVACION = 3
OPCION_FINALIZAR = 4

ENERGIA_TERRENO = 8
PROVISIONES_TERRENO = 0
PUNTOS_TERRENO = 10

ENERGIA_MUESTRA = 12
PROVISIONES_MUESTRA = 2
PUNTOS_MUESTRA = 20

ENERGIA_OBSERVACION = 5
PROVISIONES_OBSERVACION = 0
PUNTOS_OBSERVACION = 8

# --- Entrada de datos ---
energia = int(input("Energía disponible al llegar al destino: "))
provisiones = int(input("Provisiones disponibles al llegar al destino: "))

# --- Estado inicial de la exploración ---
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
continuar_exploracion = True

# --- Ciclo del menú ---
# Se repite hasta que el usuario finalice o una actividad no pueda realizarse.
while continuar_exploracion:
    print("")
    print("=== Menú de actividades ===")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    opcion = int(input("Seleccione una opción: "))

    # --- Decisión según la opción elegida ---
    if opcion == OPCION_TERRENO:
        # Se verifican los recursos antes de ejecutar la actividad.
        if energia >= ENERGIA_TERRENO and provisiones >= PROVISIONES_TERRENO:
            energia = energia - ENERGIA_TERRENO
            provisiones = provisiones - PROVISIONES_TERRENO
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_TERRENO
            print("Actividad realizada: Analizar terreno. Puntos obtenidos:", PUNTOS_TERRENO)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuar_exploracion = False
    elif opcion == OPCION_MUESTRA:
        if energia >= ENERGIA_MUESTRA and provisiones >= PROVISIONES_MUESTRA:
            energia = energia - ENERGIA_MUESTRA
            provisiones = provisiones - PROVISIONES_MUESTRA
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_MUESTRA
            print("Actividad realizada: Recolectar muestra. Puntos obtenidos:", PUNTOS_MUESTRA)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuar_exploracion = False
    elif opcion == OPCION_OBSERVACION:
        if energia >= ENERGIA_OBSERVACION and provisiones >= PROVISIONES_OBSERVACION:
            energia = energia - ENERGIA_OBSERVACION
            provisiones = provisiones - PROVISIONES_OBSERVACION
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + PUNTOS_OBSERVACION
            print("Actividad realizada: Realizar observación. Puntos obtenidos:", PUNTOS_OBSERVACION)
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuar_exploracion = False
    elif opcion == OPCION_FINALIZAR:
        print("Exploración finalizada por la tripulación.")
        continuar_exploracion = False
    else:
        print("Opción no válida.")

# --- Salida del resumen final ---
print("")
print("Actividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia, "unidades")
print("Provisiones restantes:", provisiones, "unidades")