import requests
import allure
import pytest
from conftest import create_user

@pytest.mark.regression
@allure.title("Update User")
@allure.description("Test to update an existing user.")
def test_update_user(create_user, login):
    user_id = create_user['id']
    headers = {"Authorization": f"Bearer {login}"}

    with allure.step(f"Send PUT request to update user with ID {user_id}"):
        response = requests.put(f"https://reqres.in/api/users/{user_id}", json={"name": "John", "job": "zion resident"},
                                headers=headers)

    with allure.step("Verify the response status code is 200"):
        assert response.status_code == 200

    with allure.step("Verify the updated user's details"):
        user = response.json()
        assert user['name'] == "John"
        assert user['job'] == "zion resident"
