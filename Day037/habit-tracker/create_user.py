import requests

pixela_endpoint = "https://pixe.la/v1/users"


# create pixela user
def create_user():
    create_user_params = {
        "token": "secret",
        "username": "user",
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    with requests.post(url=pixela_endpoint, json=create_user_params) as response:
        response.raise_for_status()
        print(response.text)


# create_user()
