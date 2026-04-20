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

![Diagrama de arquitectura](media\Diagrama.png)

## Endpoints Planeados
Nuestra API contará con los siguientes endpoints principales:

**Gestión de Usuarios**
* `POST /usuarios`: Registra un nuevo usuario en la base de datos.
* `GET /usuarios/{id_usuario}`: Obtiene el perfil de un usuario específico.

**Gestión de Clima**
* `GET /clima/{ciudad}`: Obtiene el clima actual de una ciudad por nombre.
* `GET /clima/coordenadas`: Obtiene el clima actual basado en latitud y longitud (`lat`, `lon` como query parameters).
* `GET /clima/pronostico/{ciudad}`: Obtiene el pronóstico del clima de los próximos 5 días para una ciudad.

**Gestión de Favoritos**
* `POST /favoritos`: Guarda una nueva ubicación favorita en la base de datos para un usuario.
* `GET /favoritos/{id_usuario}`: Recupera la lista de ciudades favoritas de un usuario.
* `DELETE /favoritos/{id_ciudad}`: Elimina una ciudad de la lista de favoritos.
* `GET /clima/favoritos/{id_usuario}`: Obtiene el clima actual de todas las ciudades favoritas de un usuario en una sola petición.

**Sistema**
* `GET /health`: Comprueba el estado de la API y conexión a base de datos.

## Modelo de Datos
Usaremos un modelo relacional en MySQL.
### Tabla: `usuarios`
Almacena la información básica de las personas que utilizan la API.

| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | INT | **Primary Key** (Auto-incremental) | Identificador único del usuario. |
| `nombre` | VARCHAR(100) | NOT NULL | Nombre o nickname del usuario. |
| `email` | VARCHAR(150) | UNIQUE, NOT NULL | Correo electrónico del usuario (identificador único real). |
| `unidad_medida` | ENUM | DEFAULT 'metric' | Preferencia del usuario ('metric' para Celsius, 'imperial' para Fahrenheit). |
| `fecha_registro` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Fecha y hora en que se registró. |
| `activo` | BOOLEAN | DEFAULT TRUE | Permite "borrado lógico" (soft delete) del usuario. |

### Tabla: `ubicaciones_favoritas`
Conecta a un usuario específico con las ciudades de las que quiere consultar el clima.

| Campo | Tipo de Dato | Restricciones | Descripción |
| :--- | :--- | :--- | :--- |
| `id` | INT | **Primary Key** (Auto-incremental) | Identificador único del registro. |
| `usuario_id` | INT | **Foreign Key** (Ref: `usuarios.id`) | Relación con el usuario dueño de la ubicación. |
| `ciudad` | VARCHAR(100) | NOT NULL | Nombre de la ciudad para mostrar al usuario. |
| `lat` | DECIMAL(10,8) | NOT NULL | Latitud exacta para consultas precisas a OpenWeatherMap. |
| `lon` | DECIMAL(11,8) | NOT NULL | Longitud exacta para consultas precisas a OpenWeatherMap. |

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
