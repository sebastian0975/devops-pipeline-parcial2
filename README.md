# DevOps Pipeline - Evaluación Final Transversal

## Descripción

Este proyecto corresponde a la Evaluación Final Transversal de la asignatura **Ingeniería DevOps (DOY0101)**.

El objetivo es implementar un flujo DevOps para un microservicio desarrollado con Flask, integrando control de versiones, integración continua, pruebas automatizadas, contenedores, despliegue mediante Kubernetes y herramientas de observabilidad.

El proyecto cuenta con un pipeline CI/CD utilizando GitHub Actions, encargado de validar la calidad del código, ejecutar pruebas, realizar análisis de seguridad y construir la imagen Docker del microservicio.

---

# Tecnologías utilizadas

* Python 3.11
* Flask
* Docker
* Docker Compose
* Kubernetes
* Prometheus
* Grafana
* GitHub Actions
* Pytest
* Pytest-Cov
* Flake8
* Bandit
* Dependabot

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
      │
      ├── Docker Compose
      │       ├── Flask
      │       ├── Prometheus
      │       └── Grafana
      │
      └── Kubernetes
              ├── Deployment
              └── Service
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

# Microservicio Flask

El microservicio fue desarrollado utilizando Flask y expone los siguientes endpoints:

| Método | Endpoint   | Descripción                                 |
| ------ | ---------- | ------------------------------------------- |
| GET    | `/`        | Estado general del microservicio            |
| GET    | `/health`  | Verificación de disponibilidad              |
| GET    | `/metrics` | Exposición de métricas para Prometheus      |
| GET    | `/error`   | Generación controlada de error para pruebas |

---

# Pipeline CI/CD

El pipeline implementado mediante GitHub Actions realiza:

* Instalación de dependencias.
* Ejecución de pruebas automatizadas con Pytest.
* Generación de reporte de cobertura.
* Validación de calidad mediante Flake8.
* Análisis de seguridad mediante Bandit.
* Construcción de imagen Docker.
* Ejecución de validación del contenedor.

Estas etapas permiten detectar errores antes de continuar con las siguientes fases del flujo.

---

# Observabilidad

La observabilidad se implementa utilizando Prometheus y Grafana.

Prometheus obtiene las métricas desde el endpoint:

```
/metrics
```

Grafana utiliza Prometheus como fuente de datos para visualizar el estado del microservicio.

Las métricas visualizadas incluyen:

* Cantidad total de peticiones.
* Cantidad total de errores.
* Cantidad de health checks.
* Tiempo promedio de respuesta.
* Métricas de recursos del proceso.

---

# Métricas implementadas

El microservicio utiliza `prometheus_client` para generar métricas:

* `peticiones_totales`
* `errores_totales`
* `health_checks_totales`
* `tiempo_respuesta_segundos`

Estas métricas permiten observar el comportamiento del servicio durante su ejecución.

---

# Contenedores

El proyecto utiliza Docker para contenerizar el microservicio Flask.

Docker Compose permite ejecutar los servicios:

* Microservicio Flask.
* Prometheus.
* Grafana.

---

# Kubernetes

El despliegue en Kubernetes utiliza los siguientes recursos:

* Namespace.
* Deployment.
* Service tipo NodePort.

El microservicio se ejecuta dentro del namespace:

```
devops
```

Comandos utilizados para validar el despliegue:

```
kubectl get pods -n devops

kubectl get svc -n devops
```

---

# Evidencias

Las evidencias del funcionamiento del proyecto se encuentran en:

```
docs/evidencias
```

Incluyen capturas de:

* Ejecución del pipeline GitHub Actions.
* Dashboard Grafana.
* Targets de Prometheus.
* Estado de Kubernetes.
* Ejecución del microservicio.

---

# Ejecución local

## Docker Compose

Ejecutar:

```
docker compose up --build
```

Servicios disponibles:

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

# Pruebas

Ejecutar:

```
pytest --cov=app
```

Validación de calidad:

```
flake8 app
```

Análisis de seguridad:

```
bandit -r app
```

---

# Autor

**Sebastián González Tapia**

Ingeniería en Informática

Duoc UC
