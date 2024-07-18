import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("List Resources")
@allure.description("Test to list all resources.")
def test_list_resource():
    with allure.step("Send GET request to list resources"):
        response = requests.get("https://reqres.in/api/unknown")

    with allure.step("Verify the response status code"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'data' key"):
        assert 'data' in response.json()