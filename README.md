# DevOps Pipeline - Evaluación Parcial 2

## Descripción del proyecto

Este proyecto consiste en un microservicio desarrollado con Flask en el contexto de la asignatura de Ingeniería DevOps.  
El objetivo es implementar un pipeline CI/CD que automatice el proceso de integración, pruebas, construcción con Docker y despliegue en un entorno simulado mediante Docker Compose.

---

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

---

## Estructura del proyecto

- app/ → Código del microservicio Flask
- tests/ → Pruebas automatizadas
- .github/workflows/ → Pipeline CI/CD (GitHub Actions)
- Dockerfile → Imagen del microservicio
- docker-compose.yml → Orquestación del entorno simulado

---

## Funcionalidad

El microservicio expone la ruta:

GET /

Respuesta esperada:

```json
{"mensaje": "Microservicio DevOps funcionando"}
```

---

## Ejecución del proyecto

### 1. Con Docker Compose (recomendado)

```bash
docker compose up --build
```

El servicio quedará disponible en:
http://localhost:5000

---

### 2. Con Docker directamente

```bash
docker build -t microservicio-devops .
docker run -p 5000:5000 microservicio-devops
```

---

## Ejecución de pruebas

```bash
pytest --cov=app
```

---

## Pipeline CI/CD (GitHub Actions)

El pipeline se ejecuta automáticamente en cada push o pull request a las ramas main o develop.

Incluye las siguientes etapas:

1. Instalación de dependencias
2. Ejecución de pruebas automatizadas (pytest)
3. Análisis de cobertura de código (pytest-cov)
4. Análisis de calidad de código (flake8)
5. Análisis de dependencias (Dependabot - SCA)
6. Construcción de imagen Docker
7. Ejecución del contenedor en entorno simulado

Esto permite asegurar calidad, trazabilidad y funcionamiento del sistema antes del despliegue.

---

## Docker Compose (orquestación)

El archivo docker-compose.yml permite levantar el sistema completo en un entorno simulado.

Incluye:
- Servicio del microservicio Flask
- Exposición del puerto 5000
- Variables de entorno (si aplica)
- Red interna entre contenedores
- Healthcheck para validar estado del servicio
- Reinicio automático en caso de fallos

---

## Seguridad y dependencias (SCA)

Se utiliza Dependabot para el análisis automático de dependencias del proyecto.

Esto permite detectar vulnerabilidades en librerías utilizadas y mantener el proyecto actualizado y seguro.

---

## Aprendizaje

Se logró implementar un pipeline CI/CD funcional utilizando GitHub Actions, integrando pruebas automatizadas, análisis de calidad de código y construcción de imágenes Docker.

También se comprendió la importancia de la orquestación de contenedores con Docker Compose para simular entornos reales de despliegue.

---

## Autor

Sebastián González Tapia