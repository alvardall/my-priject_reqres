import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("Register User - Unsuccessful")
@allure.description("Test to register a new user with missing data.")
def test_register_unsuccessful():
    with allure.step("Send POST request to register a new user with missing data"):
        response = requests.post("https://reqres.in/api/register", json={"email": "sydney@fife"})

    with allure.step("Verify the response status code is 400"):
        assert response.status_code == 400

    with allure.step("Verify the response contains 'error'"):
        assert 'error' in response.json()
