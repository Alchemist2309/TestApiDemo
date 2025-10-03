```markdown
# TestApiDemo

Repositorio de demostración para una API simple + ejercicios de lógica en Python.

## 🧾 Tabla de contenido

- [Descripción](#descripción)  
- [Estructura del proyecto](#estructura-del-proyecto)  
- [Requisitos](#requisitos)  
- [Instalación](#instalación)  
- [Uso](#uso)  
  - [API (api.py)](#api-apipy)  
  - [Ejercicios de lógica (ejercicios_logica.py)](#ejercicios-de-lógica-ejercicios_logicapy)  
- [Contribuciones](#contribuciones)  
- [Licencia](#licencia)  

---

## Descripción

Este proyecto es un entorno de prueba que combina dos componentes:

1. Una API básica (con `api.py`) para demostrar consultas o endpoints simples.  
2. Un conjunto de ejercicios de lógica en Python (en `ejercicios_logica.py`) que implementan funciones como:
   - Verificar si un número es primo  
   - Ordenar palabras en una cadena  
   - Verificar si una cadena es palíndromo  
   - Generar la secuencia de Fibonacci  
   - Buscar dos números cuya suma sea un objetivo  

Este repositorio sirve como proyecto de ejemplo, para pruebas, enseñanza o como base para ampliaciones.

---

## Estructura del proyecto

```

TestApiDemo/
├── api.py
├── ejercicios_logica.py
├── README.md


````

- `api.py` — contiene los endpoints / lógica de la API.  
- `ejercicios_logica.py` — contiene las funciones de lógica que implementan los retos descritos.  
- `README.md` — este archivo, con documentación del proyecto.

---

## Requisitos

- Python 3.7+  
- (Opcional) Virtual environment para aislar dependencias  



---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/Alchemist2309/TestApiDemo.git
   cd TestApiDemo
   ```


---

## Uso

### API (api.py)

Ejecuta:

```bash
pytest -v api.py 
```

### Ejercicios de lógica (ejercicios_logica.py)

Ejemplo de uso

```bash
python3 ejercicios_logica.py 
```
