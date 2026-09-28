# Misión Órbita

Simulador básico de exploración espacial en Python, desarrollado para el curso
**SOFT-01 Principios de Programación 1** (Sección SCV3, Periodo C3-2026),
Universidad CENFOTEC. Docente: Verónica Mora Lezcano.

Este repositorio corresponde al **Avance 1: Preparación de la misión**.

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
    └── documentacion/
        └── avance1.pdf

## Descripción de los ejercicios

1. **Ejercicio 1:** cálculo de recursos necesarios para una misión (flujo secuencial).
2. **Ejercicio 2:** verificación de combustible (condicional simple).
3. **Ejercicio 3:** verificación del soporte para la tripulación (condicional doble).
4. **Ejercicio 4:** autorización inicial de lanzamiento (condicional doble sin anidación).

## Cómo ejecutar los programas

Requisito: Python 3 instalado.

    cd avance1
    python ejercicio1_recursos.py
    python ejercicio2_combustible.py
    python ejercicio3_soporte_tripulacion.py
    python ejercicio4_autorizacion.py

En algunos sistemas el comando es `python3` en lugar de `python`.

## Convenciones y estilos

- Archivos `.py` elaborados en Visual Studio Code.
- Variables en `snake_case` y en minúscula.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo.
- Sin números mágicos dentro de las fórmulas.
- Indentación de 4 espacios.
- Encabezado de comentarios en cada archivo (archivo, curso, integrantes, fecha, versión y descripción).
- Comentarios antes de cada bloque lógico explicando el porqué.
- Mensajes de commit descriptivos, en español y en presente (ej. "Agrega tabla de variables del ejercicio 2").
