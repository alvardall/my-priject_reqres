import requests
import allure
import pytest
from conftest import create_user

@pytest.mark.regression
@allure.title("Patch User")
@allure.description("Test to partially update an existing user.")
def test_patch_user(create_user, login):
    user_id = create_user['id']
    headers = {"Authorization": f"Bearer {login}"}

    with allure.step(f"Send PATCH request to partially update user with ID {user_id}"):
        response = requests.patch(f"https://reqres.in/api/users/{user_id}",
                                  json={"name": "John", "job": "zion resident"}, headers=headers)

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the updated user's details"):
        user = response.json()
        assert user['name'] == "John"
        assert user['job'] == "zion resident"
