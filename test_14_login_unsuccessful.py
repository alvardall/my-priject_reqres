import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("Login - Unsuccessful")
@allure.description("Test to login with invalid credentials.")
def test_login_unsuccessful():
    with allure.step("Send POST request to login with invalid credentials"):
        response = requests.post("https://reqres.in/api/login", json={"email": "peter@klaven"})

    with allure.step("Verify the response status code is 400"):
        assert response.status_code == 400

    with allure.step("Verify the response contains 'error'"):
        assert 'error' in response.json()
