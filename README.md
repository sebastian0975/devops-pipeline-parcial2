# DevOps Pipeline - Evaluación Parcial 3

## Descripción

Este proyecto corresponde a la Evaluación Parcial 3 de la asignatura de Ingeniería DevOps.

Consiste en la extensión del pipeline DevOps desarrollado previamente para incorporar herramientas de observabilidad mediante Prometheus y Grafana, permitiendo monitorear el comportamiento del microservicio y visualizar métricas de funcionamiento en un entorno simulado.

Además, el proyecto incluye un despliegue del microservicio utilizando Docker, Docker Compose y Kubernetes.

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
* pytest-cov
* Flake8
* Bandit
* Dependabot

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

Expone las siguientes rutas:

## GET /

Devuelve el estado del microservicio.

Respuesta:

```json
{
  "mensaje": "Microservicio DevOps funcionando",
  "estado": "OK"
}
```

## GET /error

Genera un error controlado para registrar una métrica de errores.

## GET /metrics

Expone las métricas del microservicio en formato Prometheus.

---

# Observabilidad

Se implementó Prometheus para recolectar las métricas generadas por el microservicio.

Las métricas son obtenidas desde:

```
/metrics
```

Grafana fue configurado como herramienta de visualización utilizando Prometheus como fuente de datos.

Se creó un dashboard personalizado que muestra:

* Peticiones Totales
* Errores Totales
* CPU del proceso
* Memoria utilizada

---

# Kubernetes

El proyecto incluye manifiestos para desplegar el microservicio en un clúster Kubernetes.

Se implementan los siguientes recursos:

* Namespace
* Deployment
* Service (NodePort)

El despliegue fue validado verificando el estado del Pod y del Deployment.

---

# Pipeline CI/CD

El proyecto incorpora un pipeline utilizando GitHub Actions.

El flujo realiza las siguientes tareas:

* Instalación de dependencias
* Ejecución de pruebas automatizadas
* Cobertura de código con pytest-cov
* Análisis de calidad con Flake8
* Escaneo de seguridad mediante Bandit
* Construcción de la imagen Docker
* Ejecución del contenedor

---

# Evidencias

Las evidencias del funcionamiento del proyecto se encuentran en:

```
docs/evidencias
```

Incluyen capturas de:

* Dashboard de Grafana
* Estado de Prometheus
* Contenedores Docker
* Recursos de Kubernetes
* Pipeline de GitHub Actions

---

# Ejecución del proyecto

## Docker Compose

```bash
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

```bash
pytest --cov=app
```

---

# Autor

Sebastián González Tapia
