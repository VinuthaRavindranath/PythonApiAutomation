import requests
from faker import Faker

fake = Faker()

baseUri = 'https://gorest.co.in'
bearer_token = "your token"
headers = {"Authorization": f"Bearer {bearer_token}"}
json = {"status": "inactive"}


def user_creation_update_and_retrival(name, gender, email, status):
    response = requests.post(f'{baseUri}/public/v2/users/', json={
        "name": name,
        "gender": gender,
        "email": email,
        "status": status
    }, headers=headers)
    if response.status_code == 201:
        new_user = response.json()
        user_id = new_user['id']
        update_response = requests.put(f'{baseUri}/public/v2/users/{user_id}', headers=headers, json=json)
        if update_response.status_code == 200:
            get_response = requests.get(f'{baseUri}/public/v2/users/{user_id}', headers=headers)
            if get_response.status_code == 200:
                user_data = get_response.json()
                assert user_data[
                           'status'] == "inactive", f"user status to be inactive but received {user_data['status']}"
            else:
                return f"Error: {response.status_code}"
    else:
        return f"Error: {response.status_code}"


user_creation_update_and_retrival(fake.name(), "male", fake.email(), "active")

