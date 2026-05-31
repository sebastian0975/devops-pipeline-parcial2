from app.app import app

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get("/")

    assert respuesta.status_code == 200
    assert "mensaje" in respuesta.get_json()