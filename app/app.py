from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)


REQUEST_COUNT = Counter(
    "peticiones_totales",
    "Cantidad total de peticiones al microservicio"
)


ERROR_COUNT = Counter(
    "errores_totales",
    "Cantidad total de errores del microservicio"
)


@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "mensaje": "Microservicio DevOps funcionando",
        "estado": "OK"
    })


@app.route("/error")
def error():
    ERROR_COUNT.inc()
    return "Error simulado", 500


@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    