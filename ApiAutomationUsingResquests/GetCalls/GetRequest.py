import requests
import pprint

baseUri = "https://gorest.co.in"


def get_all_users():
    response = requests.get(f"{baseUri}/public/v2/users")
    pprint.pprint(response.json())
    assert response.status_code == 200, f"{response.status_code} api failed"


get_all_users()


def get_all_users2():
    response = requests.get(f"{baseUri}/public/v2/users")
    if response.status_code == 200:
        users = response.json()
        first_user_id = users[0]['id']
        email = users[0]['email']
        assert isinstance(first_user_id, int) == True, "invalid id"
        assert email.count('@') == 1, " invalid email-id"


get_all_users2()
