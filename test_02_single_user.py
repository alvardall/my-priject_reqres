import requests
import allure
import pytest
from conftest import create_user


@pytest.mark.regression
@allure.title("Get Single User")
@allure.description("Test to get a single user by ID.")
def test_single_user():
    user_id = 1

    with allure.step(f"Send GET request to get user with ID {user_id}"):
        response = requests.get(f"https://reqres.in/api/users/{user_id}")

    with allure.step("Verify the response status code"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'data' key"):
        assert 'data' in response.json()