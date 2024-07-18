import requests
import allure
import pytest


@pytest.mark.regression
@allure.title("Single Resource Not Found")
@allure.description("Test to get a non-existent resource.")
def test_single_resource_not_found():
    with allure.step("Send GET request to get non-existent resource"):
        response = requests.get("https://reqres.in/api/unknown/23")

    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404