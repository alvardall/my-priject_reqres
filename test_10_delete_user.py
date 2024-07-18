import requests
import allure
import pytest
from conftest import create_user

@pytest.mark.regression
@allure.title("Delete User")
@allure.description("Test to delete an existing user.")
def test_delete_user(create_user, login):
    user_id = create_user['id']
    headers = {"Authorization": f"Bearer {login}"}

    with allure.step(f"Send DELETE request to delete user with ID {user_id}"):
        response = requests.delete(f"https://reqres.in/api/users/{user_id}", headers=headers)

    with allure.step("Verify the response status code is 204"):
        assert response.status_code == 204