# TRABAJO_FINAL_LOGICA
# Sistema de Control de Almuerzos

Proyecto Integrador — Introducción a la Programación
Universidad Internacional del Ecuador — UIDE

---

## Integrantes

- Quinto Moreno María José

## Objetivo

Automatizar el registro y control de consumo de almuerzos en una empresa o institución, validando la identidad de cada persona, controlando que no repita almuerzo en el mismo día y generando reportes de consumo diario, mensual y por empresa para facilitar el cobro.

## Funcionalidades

- Registro de almuerzo por cédula con selección de sopa ($1,00), segundo ($1,50) y jugo ($0,50)
- Control de un almuerzo por persona por día
- Módulo de administrador con contraseña para registrar personas y ver el listado
- Reporte del día, reporte mensual por persona y reporte de totales por empresa
- Cierre del día que conserva el historial mensual

## Tecnologías

Python 3 — solo terminal, sin librerías externas, usando listas, diccionarios, condicionales y ciclos.

## Cómo ejecutar

```bash
python almuerzo.py
```

## Credenciales de prueba

Contrasena de administrador: `admin123`

Cedulas de prueba: 1111111111 al 9999999999 y 1234567890

## Estructura del repositorio

```
sistema-almuerzos/
├── almuerzo.py
├── README.md
└── diagramas/
    ├── diagrama_flujo_almuerzos.xml
    └── diagrama_casos_uso_almuerzos.xml
```

## Impacto tecnológico

Un control de almuerzos manual en papel genera errores de cobro y pérdida de registros. Al automatizarlo con código se elimina el error humano y se obtienen reportes precisos en segundos, demostrando cómo los fundamentos de programación tienen aplicación directa en problemas reales de empresas e instituciones.

## Fecha

28 Junio 2025
