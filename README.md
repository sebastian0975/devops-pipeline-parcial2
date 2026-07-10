# DevOps Pipeline - Evaluación Final Transversal

## Descripción

Este proyecto corresponde a la Evaluación Final Transversal de la asignatura **Ingeniería DevOps (DOY0101)**.

El objetivo es automatizar el ciclo de vida de un microservicio desarrollado en Flask aplicando principios DevOps, integrando control de versiones, integración continua, contenedores, orquestación, monitoreo, observabilidad, métricas y controles de calidad.

El proyecto implementa un pipeline CI/CD que permite validar automáticamente el código antes de construir y desplegar la aplicación.

---

# Tecnologías utilizadas

- Python 3.11
- Flask
- Docker
- Docker Compose
- Kubernetes
- Prometheus
- Grafana
- GitHub Actions
- Pytest
- Pytest-Cov
- Flake8
- Bandit
- Dependabot

---

# Arquitectura del proyecto

```
Desarrollador
      │
      ▼
 GitHub Repository
      │
      ▼
 GitHub Actions
      │
      ├── Pytest
      ├── Flake8
      ├── Bandit
      ▼
 Docker Build
      ▼
 Docker Compose
      │
      ├── Microservicio Flask
      ├── Prometheus
      └── Grafana
```

---

# Estructura del proyecto

```
.
├── .github/
│   └── workflows/
├── app/
├── docs/
│   └── evidencias/
├── grafana/
├── kubernetes/
├── prometheus/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# Funcionalidad del microservicio

El microservicio fue desarrollado utilizando Flask.

Actualmente expone los siguientes endpoints:

| Método | Endpoint | Descripción |
|---------|----------|-------------|
| GET | / | Estado del microservicio |
| GET | /health | Verificación de disponibilidad |
| GET | /metrics | Métricas Prometheus |
| GET | /error | Genera un error controlado para pruebas |

---

# Pipeline CI/CD

El pipeline automatiza las siguientes tareas:

- Instalación de dependencias.
- Ejecución de pruebas unitarias.
- Medición de cobertura.
- Análisis de calidad con Flake8.
- Escaneo de seguridad con Bandit.
- Construcción de la imagen Docker.
- Ejecución del contenedor únicamente cuando todas las validaciones anteriores son exitosas.

De esta manera se evita desplegar versiones con errores de calidad o problemas de seguridad.

---

# Observabilidad

La observabilidad del proyecto se implementa mediante Prometheus y Grafana.

Prometheus obtiene las métricas directamente desde:

```
/metrics
```

Grafana utiliza Prometheus como fuente de datos y permite visualizar el comportamiento del microservicio en tiempo real.

Las métricas monitoreadas incluyen:

- Total de peticiones.
- Total de errores.
- Uso de CPU.
- Uso de memoria.
- Disponibilidad del servicio.

---

# Decisiones técnicas

Las métricas permiten apoyar decisiones durante la operación del sistema.

Ejemplos:

- Un aumento en la cantidad de errores puede indicar un problema en una nueva versión del microservicio.
- Un incremento sostenido del uso de CPU puede justificar aumentar los recursos asignados al contenedor.
- Un crecimiento del consumo de memoria puede evidenciar fugas de memoria.
- La disponibilidad del servicio permite detectar caídas del microservicio rápidamente.
- Los resultados de Flake8 y Bandit permiten impedir despliegues que no cumplan los estándares de calidad y seguridad.

---

# Contenedores

El proyecto utiliza Docker para contenerizar el microservicio.

Docker Compose permite ejecutar automáticamente:

- Microservicio Flask.
- Prometheus.
- Grafana.

---

# Kubernetes

Se incluyen manifiestos para desplegar el microservicio utilizando Kubernetes.

Los recursos implementados son:

- Namespace
- Deployment
- Service

---

# Evidencias

Las evidencias del funcionamiento del proyecto se encuentran en:

```
docs/evidencias
```

Incluyen capturas de:

- Dashboard Grafana.
- Prometheus Targets.
- Docker Compose.
- Kubernetes.
- Pipeline GitHub Actions.

---

# Ejecución

## Docker Compose

```
docker compose up --build
```

Microservicio:

```
http://localhost:5000
```

Prometheus:

```
http://localhost:9090
```

Grafana:

```
http://localhost:3000
```

---

# Ejecución de pruebas

```
pytest --cov=app
```

---

# Autor

**Sebastián González Tapia**

Ingeniería en Informática

Duoc UC