import requests
import allure
import pytest


@pytest.mark.regression
@allure.title("Get Single Resource")
@allure.description("Test to get a single resource by ID.")
def test_single_resource():
    with allure.step("Send GET request to get resource with ID 2"):
        response = requests.get("https://reqres.in/api/unknown/2")

    with allure.step("Verify the response status code"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'data' key"):
        assert 'data' in response.json()