# API de Clima - Proyecto Integrador

[![CI Pipeline Status](https://github.com/BJD23/API_Weather/actions/workflows/ci.yml/badge.svg)](https://github.com/BJD23/API_Weather/actions)

## Descripción del Proyecto
Esta es una API RESTful desarrollada como proyecto integrador para la experiencia educativa de Despliegue de Software (LIS 601). La API consume datos en tiempo real desde **OpenWeatherMap** permite a los usuarios consultar el clima, además de guardar sus ubicaciones favoritas en una base de datos **MySQL**.

Todo el proyecto está contenedorizado con Docker y cuenta con un pipeline de Integración y Despliegue Continuo (CI/CD) usando GitHub Actions.

## Arquitectura y Tecnologías
* **Backend:** Python con FastAPI.
* **Base de Datos:** MySQL.
* **Contenedores:** Docker y Docker Compose.
* **CI/CD:** GitHub Actions.
* **API Externa:** OpenWeatherMap.

*(Nota para el equipo: Aquí insertaremos la imagen de nuestro diagrama de arquitectura en la Fase 1)*.

## Endpoints Planeados
Nuestra API contará con los siguientes endpoints principales:

* `GET /clima/{ciudad}`: Obtiene el clima actual de una ciudad consultando OpenWeatherMap.
* `POST /favoritos`: Guarda una nueva ubicación favorita en la base de datos para un usuario.
* `GET /favoritos/{id_usuario}`: Recupera la lista de ciudades favoritas de un usuario.
* `DELETE /favoritos/{id_ciudad}`: Elimina una ciudad de la lista de favoritos.

## Modelo de Datos
Usaremos un modelo relacional en MySQL.
### Tabla: `usuarios`
Almacena la información básica de las personas que utilizan la API.

| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | INT | **Primary Key** (Auto-incremental) | Identificador único del usuario. |
| `nombre` | VARCHAR(100) | NOT NULL | Nombre o nickname del usuario. |
| `fecha_registro` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Fecha y hora en que se registró. |

### Tabla: `ubicaciones_favoritas`
Conecta a un usuario específico con las ciudades de las que quiere consultar el clima.

| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | INT | **Primary Key** (Auto-incremental) | Identificador único del registro. |
| `usuario_id` | INT | **Foreign Key** (Ref: `usuarios.id`) | Relación con el usuario dueño de la ubicación. |
| `ciudad` | VARCHAR(100) | NOT NULL | Nombre de la ciudad (ej. "Coatzacoalcos"). |

## Cómo levantar el proyecto localmente

Para correr esta API en tu máquina local, no necesitas instalar dependencias de código, solo tener **Docker** instalado.

1. Clona este repositorio:
   `git clone https://github.com/BJD23/API_Weather.git`

2. Construye y levanta los contenedores con Docker:
   `docker compose up --build`

La API estará disponible en `http://localhost:8000`.

## Equipo de Trabajo
 
* **[Carlos Sebastian Cazarin Legy]** - Backend Developer & API Lead  | zs23028293@estudiantes.uv.mx
* **[Héctor Favio Jiménez Ramos]** - DBA & DevOps Engineer  | zs23021812@estudiantes.uv.mx 
* **[Roberto Carlos Beltrán Guevara]** - QA Engineer & Technical Writer  | zs23017354@estudiantes.uv.mx 

---
**Universidad Veracruzana** | Licenciatura en Ingeniería de Software 
