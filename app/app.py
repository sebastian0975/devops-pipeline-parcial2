from flask import Flask, jsonify
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "peticiones_totales",
    "Cantidad total de peticiones al microservicio",
)

ERROR_COUNT = Counter(
    "errores_totales",
    "Cantidad total de errores del microservicio",
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    logger.info("Se recibió una petición en la ruta principal (/)")
    return jsonify(
        {
            "mensaje": "Microservicio DevOps funcionando",
            "estado": "OK",
        }
    )


@app.route("/error")
def error():
    ERROR_COUNT.inc()
    logger.error("Se produjo un error simulado")
    return "Error simulado", 500


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST,
    }


if __name__ == "__main__":
    logger.info("Microservicio iniciado correctamente")
    app.run(host="0.0.0.0", port=5000)  # nosec B104
    