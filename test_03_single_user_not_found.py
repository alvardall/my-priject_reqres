import requests
import allure
import pytest


@pytest.mark.regression
@allure.title("Single User Not Found")
@allure.description("Test to get a non-existent user.")
def test_single_user_not_found():
    with allure.step("Send GET request to get non-existent user"):
        response = requests.get("https://reqres.in/api/users/23")

    with allure.step("Verify the response status code is 404"):
        assert response.status_code == 404