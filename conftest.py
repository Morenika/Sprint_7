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
    # create (setup)
    create_resp = CourierApi.create(courier_data)
    if create_resp.status_code != 201:
        raise RuntimeError(
            f"Courier creation failed in fixture: {create_resp.status_code}, {create_resp.text}"
        )

    # login (to get id for cleanup)
    login_resp = CourierApi.login({
        "login": courier_data["login"],
        "password": courier_data["password"]
    })
    if login_resp.status_code != 200 or "id" not in login_resp.json():
        raise RuntimeError(
            f"Courier login failed in fixture: {login_resp.status_code}, {login_resp.text}"
        )

    courier_id = login_resp.json()["id"]

    yield {**courier_data, "id": courier_id}

    # cleanup
    CourierApi.delete(courier_id)
