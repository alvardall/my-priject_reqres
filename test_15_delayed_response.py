import requests
import allure
import pytest


@pytest.mark.regression
@allure.title("Delayed Response")
@allure.description("Test to get a delayed response from the server.")
def test_delayed_response():
    with allure.step("Send GET request to get a delayed response"):
        response = requests.get("https://reqres.in/api/users?delay=3")

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'data'"):
        assert 'data' in response.json()