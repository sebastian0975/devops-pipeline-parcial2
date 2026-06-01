# DevOps Pipeline - Evaluación 2

## Descripción del proyecto

Este proyecto consiste en un microservicio desarrollado con Flask como parte de la asignatura de Ingeniería DevOps.

El objetivo es implementar un pipeline CI/CD que automatice el proceso de integración, pruebas, construcción con Docker y despliegue en un entorno simulado.

## Tecnologías utilizadas

- Python 3.11
- Flask
- Docker
- Docker Compose
- Pytest
- GitHub Actions
- Flake8
- pytest-cov
- Dependabot

## Estructura del proyecto

- app/ → código del microservicio
- tests/ → pruebas automatizadas
- .github/workflows/ → pipeline CI/CD
- Dockerfile → imagen del proyecto
- docker-compose.yml → entorno simulado

## Funcionalidad

El microservicio responde en la ruta:

/

Respuesta esperada:

```json
{"mensaje": "Microservicio DevOps funcionando"}
```

## Pipeline CI/CD

El pipeline se ejecuta automáticamente en GitHub Actions cuando hay push o pull request a main o develop.

Incluye:
- Instalación de dependencias
- Ejecución de tests con pytest
- Cobertura de código con pytest-cov
- Revisión de calidad con flake8
- Construcción de imagen Docker
- Ejecución del contenedor

## Ejecución con Docker

docker build -t microservicio-devops .
docker run -p 5000:5000 microservicio-devops

## Ejecución de pruebas

pytest --cov=app

## Seguridad

Se utiliza Dependabot para detectar vulnerabilidades en dependencias.

## Aprendizaje

Se aprendió a usar pipelines CI/CD, pruebas automáticas y Docker para simular despliegues.

## Autor

Sebastian Gonzalez Tapia