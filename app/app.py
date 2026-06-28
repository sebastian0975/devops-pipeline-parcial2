from flask import Flask, jsonify
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# =========================
# MÉTRICAS PROMETHEUS
# =========================

# Contador de peticiones
REQUEST_COUNT = Counter(
    "peticiones_totales",
    "Cantidad total de peticiones al microservicio"
)

# Contador de errores (NUEVO - NECESARIO PARA EVALUACIÓN 3)
ERROR_COUNT = Counter(
    "errores_totales",
    "Cantidad total de errores del microservicio"
)


# =========================
# ENDPOINT PRINCIPAL
# =========================

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return jsonify({
        "mensaje": "Microservicio DevOps funcionando",
        "estado": "OK"
    })


# =========================
# ENDPOINT DE ERROR (NUEVO)
# =========================

@app.route("/error")
def error():
    ERROR_COUNT.inc()
    return "Error simulado", 500


# =========================
# MÉTRICAS PROMETHEUS
# =========================

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {
        "Content-Type": CONTENT_TYPE_LATEST
    }


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)