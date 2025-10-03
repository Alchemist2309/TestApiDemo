import requests
import pytest
from jsonschema import validate

BASE_URL = "https://reqres.in/api"

@pytest.fixture
def user_data():
    return {
        "name": "Test User",
        "job": "Automation Engineer"
    }


def test_create_user(user_data):
    # POST /users
    response = requests.post(f"{BASE_URL}/users", json=user_data)

    # Validar código de estado
    assert response.status_code == 201

    # Validar contrato (schema)
    body = response.json()
    validate(instance=body, schema=create_user_schema)

    # Validar datos enviados
    assert body["name"] == user_data["name"]
    assert body["job"] == user_data["job"]

# Extraer ID
    user_id = body["id"]
    assert user_id is not None

    # GET /users/{id}
    get_response = requests.get(f"{BASE_URL}/users/{user_id}")

    # Como reqres no persiste datos, el usuario creado no se guarda realmente
    # Entonces GET devuelve un 404. En un API real debería devolver 200.
    # Aquí lo dejamos documentado:
    if get_response.status_code == 200:
        data = get_response.json()
        assert data["data"]["name"] == user_data["name"]
        assert data["data"]["job"] == user_data["job"]
    else:
        # Caso adicional: validar comportamiento cuando no existe
        assert get_response.status_code in [200, 404]

# Caso adicional: crear usuario con datos vacíos
def test_create_user_with_empty_data():
    response = requests.post(f"{BASE_URL}/users", json={})
    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert "createdAt" in body
