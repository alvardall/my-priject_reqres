import pytest
import requests

BASE_URL = "https://reqres.in/api"


@pytest.fixture(scope="session")
def login():
    response = requests.post(f"{BASE_URL}/login", json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    assert response.status_code == 200
    token = response.json()['token']
    return token


@pytest.fixture(scope="session")
def create_user(login):
    headers = {"Authorization": f"Bearer {login}"}
    response = requests.post(f"{BASE_URL}/users", json={"name": "John", "job": "leader"}, headers=headers)
    assert response.status_code == 201
    user = response.json()
    yield user
    user_id = user['id']
    response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
    assert response.status_code == 204