# Misión Órbita

Simulador básico de exploración espacial en Python, desarrollado para el curso
**SOFT-01 Principios de Programación 1** (Sección SCV3, Periodo C3-2026),
Universidad CENFOTEC. Docente: Verónica Mora Lezcano.

Este repositorio contiene los avances del proyecto:

- **Avance 1:** Preparación de la misión.
- **Avance 2:** Ejecución de la misión.

## Integrantes
- Julian Salazar Solis

## Estructura del repositorio

    mision-orbita/
    ├── README.md
    ├── avance1/
    │   ├── ejercicio1_recursos.py
    │   ├── ejercicio2_combustible.py
    │   ├── ejercicio3_soporte_tripulacion.py
    │   └── ejercicio4_autorizacion.py
    ├── avance2/
    │   ├── ejercicio7_exploracion.py
    │   └── ejercicio8_regreso.py
    └── documentacion/
        ├── avance1.pdf
        └── avance2.pdf

## Descripción de los ejercicios

### Avance 1: Preparación de la misión

1. **Ejercicio 1:** cálculo de recursos necesarios para una misión (flujo secuencial).
2. **Ejercicio 2:** verificación de combustible (condicional simple).
3. **Ejercicio 3:** verificación del soporte para la tripulación (condicional doble).
4. **Ejercicio 4:** autorización inicial de lanzamiento (condicional doble sin anidación).

### Avance 2: Ejecución de la misión

El alcance del Avance 2 se trabaja de forma individual, por lo que incluye los ejercicios 7 y 8.

7. **Ejercicio 7:** actividades de exploración científica en el destino (menú repetitivo con ciclo `while`, condicional múltiple y anidada, contadores y acumuladores).
8. **Ejercicio 8:** evaluación del regreso y supervivencia de la tripulación (condicional para elegir entre el caso A y el caso B, ciclo para simular los días del regreso y condicionales para obtener el menor valor y los recursos limitantes).

## Cómo ejecutar los programas

Requisito: Python 3 instalado.

Avance 1:

    cd avance1
    python ejercicio1_recursos.py
    python ejercicio2_combustible.py
    python ejercicio3_soporte_tripulacion.py
    python ejercicio4_autorizacion.py

Avance 2:

    cd avance2
    python ejercicio7_exploracion.py
    python ejercicio8_regreso.py

En algunos sistemas el comando es `python3` en lugar de `python`.

Cada programa es independiente: los datos se ingresan por consola, en el orden que solicita cada programa.

## Convenciones y estilos

- Archivos `.py` elaborados en Visual Studio Code.
- Variables en `snake_case` y en minúscula.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo.
- Sin números mágicos dentro de las fórmulas.
- Indentación de 4 espacios.
- Encabezado de comentarios en cada archivo (archivo, curso, integrantes, fecha, versión y descripción).
- Comentarios antes de cada bloque lógico explicando el porqué.
- Sin funciones propias (`def`), colecciones, librerías externas, `min()`, `max()`, `break`, `continue`, `exit()` ni `quit()`.
- El ciclo `for`, si se usa, solo con `range()`; cada ciclo termina por su condición y la actualización de sus variables de control.
- Mensajes de commit descriptivos, en español y en presente (ej. "Agrega tabla de variables del ejercicio 2").

## Documentación

Los PDF de cada avance (tablas de variables, diagramas de flujo, código, casos de prueba y capturas de ejecución) están en la carpeta `documentacion/`.
