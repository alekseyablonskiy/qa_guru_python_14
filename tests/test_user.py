import requests
from requests import Response
from pytest_voluptuous import S
from schemas import schemas

base_url = "https://reqres.in/"


def test_create_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aliaksei",
            "job": "Automation",
        }
    )
    assert create_user.status_code == 201
    assert create_user.json()["name"] == "Aliaksei"
    assert create_user.json()["job"] == "Automation"
    assert S(schemas.create_single_user) == create_user.json()
    assert len(create_user.json()) == 4


def test_update_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aliaksei",
            "job": "Automation",
        }
    )
    update_user: Response = requests.put(
        url=f"{base_url}api/users/2",
        json=
        {
            "name": "Aleksey",
            "job": "Automation QA"
        }
    )
    assert update_user.status_code == 200
    assert S(schemas.update_single_user) == update_user.json()
    assert update_user.json()["name"] == "Aleksey"
    assert update_user.json()["job"] == "Automation QA"


def test_register_user():
    registrate_user: Response = requests.post(
        url=f"{base_url}api/register",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "qwerty"
        }
    )
    assert registrate_user.status_code == 200
    assert S(schemas.register_single_user) == registrate_user.json()
    assert registrate_user.json()["token"] is not None


def test_login_user():
    login_user: Response = requests.post(
        url=f"{base_url}api/login",
        json=
        {
            "email": "eve.holt@reqres.in",
            "password": "qwerty"
        }
    )
    assert login_user.status_code == 200
    assert S(schemas.login_single_user_successful) == login_user.json()
    assert len(login_user.json()["token"]) == 17


def test_delete_user():
    create_user: Response = requests.post(
        url=f"{base_url}api/users",
        json=
        {
            "name": "Aliaksei",
            "job": "Automation",
        }
    )
    delete_user: Response = requests.delete(
        url=f"{base_url}api/users/2",
    )
    assert delete_user.status_code == 204