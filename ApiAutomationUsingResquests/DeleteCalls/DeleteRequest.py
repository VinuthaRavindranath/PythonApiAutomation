import requests
from faker import Faker

fake = Faker()

baseUri = 'https://gorest.co.in'
bearer_token = "your token"
headers = {"Authorization": f"Bearer {bearer_token}"}


def userCreation_deleteUser_getUser(name, gender, email, status):
    response = requests.post(f'{baseUri}/public/v2/users/', json={
        "name": name,
        "gender": gender,
        "email": email,
        "status": status
    }, headers=headers)
    if response.status_code == 201:
        new_user = response.json()
        user_id = new_user['id']
        delete_response = requests.delete(f'{baseUri}/public/v2/users/{user_id}', headers=headers)
        if delete_response.status_code == 204:
            get_response = requests.get(f'{baseUri}/public/v2/users/{user_id}', headers=headers)
            assert get_response.status_code == 404, f"status code to be 404, but received {get_response.status_code}"
        else:
            return f"Error: {delete_response.status_code}"
    else:
        return f"Error: {response.status_code}"


userCreation_deleteUser_getUser(fake.name(), "male", fake.email(), "active")
