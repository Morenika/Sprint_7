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
def created_courier(courier_data):
    # create
    create_resp = CourierApi.create(courier_data)
    assert create_resp.status_code == 201

    # login
    login_resp = CourierApi.login({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    courier_id = login_resp.json()["id"]

    yield courier_data | {"id": courier_id}

    # cleanup
    CourierApi.delete(courier_id)
