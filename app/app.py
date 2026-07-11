from flask import Flask, jsonify, Response
from prometheus_client import (
    CONTENT_TYPE_LATEST,
    Counter,
    Histogram,
    generate_latest,
)
import logging
import time


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = Flask(__name__)


# ==========================
# Métricas Prometheus
# ==========================

REQUEST_COUNT = Counter(
    "peticiones_totales",
    "Cantidad total de peticiones al microservicio",
)

ERROR_COUNT = Counter(
    "errores_totales",
    "Cantidad total de errores del microservicio",
)

HEALTH_COUNT = Counter(
    "health_checks_totales",
    "Cantidad de verificaciones de disponibilidad",
)

REQUEST_TIME = Histogram(
    "tiempo_respuesta_segundos",
    "Tiempo de respuesta del microservicio",
)


@app.before_request
def iniciar_temporizador():
    app.start_time = time.time()


@app.after_request
def registrar_tiempo(response):
    duracion = time.time() - app.start_time
    REQUEST_TIME.observe(duracion)
    return response


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    logger.info("Solicitud recibida en '/'")

    return jsonify(
        {
            "mensaje": "Microservicio DevOps funcionando",
            "estado": "OK",
        }
    )


@app.route("/health")
def health():
    HEALTH_COUNT.inc()
    logger.info("Health Check ejecutado")

    return jsonify(
        {
            "status": "UP",
        }
    )


@app.route("/error")
def error():
    ERROR_COUNT.inc()
    logger.error("Error simulado generado")

    return jsonify(
        {
            "mensaje": "Error simulado",
        }
    ), 500


@app.route("/metrics")
def metrics():
    return Response(
        generate_latest(),
        mimetype=CONTENT_TYPE_LATEST,
    )


if __name__ == "__main__":
    logger.info("Microservicio iniciado correctamente")

    app.run(
        host="0.0.0.0",  # nosec B104
        port=5000,
    )
