# conftest.py
import pytest
import random
import string
from helpers.courier import CourierApi

def random_string(length=10):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

@pytest.fixture
def courier_data():
    return {
        "login": random_string(),
        "password": random_string(),
        "firstName": random_string()
    }

@pytest.fixture
def cleanup_courier():
    created_payload = {}

    yield created_payload

    if not created_payload:
        return

    login_resp = CourierApi.login({
        "login": created_payload["login"],
        "password": created_payload["password"]
    })
    if login_resp.status_code == 200 and "id" in login_resp.json():
        CourierApi.delete(login_resp.json()["id"])

@pytest.fixture
def created_courier(courier_data, cleanup_courier):
    # создаём курьера
    create_resp = CourierApi.create(courier_data)
    if create_resp.status_code != 201:
        raise RuntimeError(
            f"Courier creation failed in fixture: {create_resp.status_code}, {create_resp.text}"
        )

    # регистрируем данные для удаления после теста
    cleanup_courier.update(courier_data)

    # отдаём тесту логин/пароль/имя
    return courier_data
