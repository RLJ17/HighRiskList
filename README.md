# Búsqueda en Listas de Alto Riesgo - API

Este proyecto es una API REST desarrollada en Python y Flask que facilita la búsqueda automatizada de entidades en listas de alto riesgo. La API permite cruzar datos de diferentes fuentes de sanciones internacionales y listas de vigilancia para asegurar la debida diligencia. A continuación, se detallan los pasos necesarios para configurar y ejecutar la API localmente.

## Requisitos Previos

- [Python](https://www.python.org/) (se recomienda v3.8 o superior)
- [Git](https://git-scm.com/)

## Configuración del Proyecto

### 1. Clonar el Repositorio

Clona el repositorio del proyecto en tu máquina local usando el siguiente comando:

```bash
git clone https://github.com/RLJ17/HighRiskList.git
```
### 2. Abrir el Proyecto
Abre el proyecto en tu editor (Visual Studio Code).

### 3. Crear un Entorno Virtual
Crea un entorno virtual para el proyecto y actívalo:
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En MacOS/Linux
source venv/bin/activate
```

### 4. Instalar las Dependencias
Instala las dependencias necesarias usando el archivo requirements.txt:
```bash
pip install -r requirements.txt
```
### 5. Ejecutar la Aplicación

Para ejecutar la aplicación localmente, ejecuta este comando desde la carpeta raiz del proyecto:
```bash
python app/main.py
```

