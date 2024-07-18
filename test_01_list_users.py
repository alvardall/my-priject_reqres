import requests
import allure
import pytest


@pytest.mark.smoke
@allure.title("List Users")
@allure.description("Test to list all users on the second page.")
def test_list_users():
    with allure.step("Send GET request to list users on page 2"):
        response = requests.get("https://reqres.in/api/users?page=2")

    with allure.step("Verify the response status code"):
        assert response.status_code == 200

    with allure.step("Verify the response contains 'data' key"):
        assert 'data' in response.json()
