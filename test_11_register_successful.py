import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("Register User - Successful")
@allure.description("Test to register a new user with valid data.")
def test_register_successful():
    with allure.step("Send POST request to register a new user"):
        response = requests.post("https://reqres.in/api/register",
                                 json={"email": "eve.holt@reqres.in", "password": "pistol"})

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'token'"):
        assert 'token' in response.json()
