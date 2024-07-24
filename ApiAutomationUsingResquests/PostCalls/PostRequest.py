import requests
from faker import Faker

fake = Faker()

baseUri = 'https://gorest.co.in'
bearer_token = "your token"
headers = {"Authorization": f"Bearer {bearer_token}"}


def user_creation_and_retrival(name, gender, email, status):
    response = requests.post(f'{baseUri}/public/v2/users/', json={
        "name": name,
        "gender": gender,
        "email": email,
        "status": status
    }, headers=headers)
    if response.status_code == 201:
        new_user = response.json()
        user_id = new_user['id']
        get_response = requests.get(f'{baseUri}/public/v2/users/{user_id}', headers=headers)
        if get_response.status_code == 200:
            user_data = get_response.json()
            return user_data
        else:
            return f"Error: {get_response.status_code}"
    else:
        return f"Error: {response.status_code}"


user_creation_and_retrival(fake.name(), "male", fake.email(), "active")
