import requests
import allure
import pytest
from conftest import login

@pytest.mark.smoke
@allure.title("Create User")
@allure.description("Test to create a new user.")
def test_create_user(login):
    headers = {"Authorization": f"Bearer {login}"}

    with allure.step("Send POST request to create a new user"):
        response = requests.post("https://reqres.in/api/users", json={"name": "John", "job": "leader"}, headers=headers)

    with allure.step("Verify the response status code is 201"):
        assert response.status_code == 201
        user = response.json()

    with allure.step("Verify the created user's details"):
        assert user['name'] == "John"
        assert user['job'] == "leader"

    with allure.step("Cleanup: Delete the created user"):
        user_id = user['id']
        requests.delete(f"https://reqres.in/api/users/{user_id}", headers=headers)
