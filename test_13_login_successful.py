import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("Login - Successful")
@allure.description("Test to login with valid credentials.")
def test_login_successful():
    with allure.step("Send POST request to login with valid credentials"):
        response = requests.post("https://reqres.in/api/login",
                                 json={"email": "eve.holt@reqres.in", "password": "cityslicka"})

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'token'"):
        assert 'token' in response.json()