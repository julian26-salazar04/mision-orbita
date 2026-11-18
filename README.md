# Misión Órbita

Simulador de exploración espacial en Python desarrollado para el curso
SOFT-01 Principios de Programación 1 (Universidad CENFOTEC).

## Descripción

Misión Órbita es un sistema integrado que administra el ciclo completo de
una misión espacial: preparación, autorización, viaje, llegada, exploración,
evaluación del regreso y resultado final. Si la nave no puede regresar, el
sistema continúa con el análisis de la tripulación varada y el cálculo de
supervivencia. Además, guarda un historial de misiones ordenado por puntaje.

El proyecto se construyó en tres avances:

- `avance1/`: preparación de la misión (ejercicios 1 a 4).
- `avance2/`: ejecución de la misión (ejercicios 7 y 8).
- `avance3/`: sistema integrado final (`mision_orbita.py`).

## Integrante

- Julián Salazar Solís

## Curso

- SOFT-01 Principios de Programación 1, sección SCV3
- Docente: Verónica Mora Lezcano
- Periodo: C3-2026

## Convenciones y estilos de programación

- Nombres de variables y funciones en `snake_case`, descriptivos.
- Constantes en MAYÚSCULAS con guion bajo, declaradas al inicio del archivo.
- Constantes de posición (por ejemplo `OXIGENO`, `DES_DIAS`) en lugar de
  índices numéricos.
- Indentación de 4 espacios.
- Comentarios que explican el porqué de cada bloque lógico.
- Un único `return` al final de cada función que devuelve un valor.
- Sin variables globales: los datos viajan por parámetros y retornos.
- Datos en listas, tuplas y matrices (sin diccionarios).

## Instrucciones para ejecutar

1. Instalar Python 3.
2. Clonar el repositorio:
   `git clone https://github.com/julian26-salazar04/mision-orbita.git`
3. Entrar a la carpeta del avance 3:
   `cd mision-orbita/avance3`
4. Ejecutar el programa:
   `python mision_orbita.py`
5. Seguir las instrucciones del menú en la consola.

## Estructura del repositorio

```
mision-orbita/
├── README.md
├── .gitignore
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
├── avance2/
│   ├── ejercicio7_exploracion.py
│   └── ejercicio8_regreso.py
├── avance3/
│   └── mision_orbita.py
└── documentacion/
    ├── Avance_1JulianSalazarSolis.pdf
    ├── Avance_2_JulianSalazarSolis.pdf
    ├── avance3_mision_orbita.pdf
    ├── ejercicio1_diagrama.png
    ├── ejercicio2_diagrama.png
    ├── ejercicio3_diagrama.png
    ├── ejercicio4_diagrama.png
    ├── ejercicio7_diagrama.png
    └── ejercicio8_diagrama.png
```

## Documentación

La carpeta `documentacion/` contiene:

- Los PDF de entrega de los avances 1, 2 y 3.
- Los diagramas de flujo de los ejercicios de los avances 1 y 2 (imágenes PNG).
- En el PDF del avance 3: tabla de variables por función, diagramas de
  flujo, código, casos de prueba con capturas y tabla de cambios.
