# DevOps Pipeline Parcial 2

## Descripción
Microservicio Flask con CI/CD usando GitHub Actions, Docker y pruebas automatizadas.

## Tecnologías
- Python
- Flask
- Pytest
- Docker
- Docker Compose
- GitHub Actions

## Cómo ejecutar el proyecto

### Docker Compose
docker-compose up --build

### Ejecución manual
python app/app.py

La aplicación corre en:
http://localhost:5000

## Pruebas
pytest

## CI/CD Pipeline
El pipeline automatiza:
- Instalación de dependencias
- Ejecución de pruebas con pytest
- Construcción de imagen Docker
- Integración continua con GitHub Actions

## Autor
Proyecto de evaluación DevOps
