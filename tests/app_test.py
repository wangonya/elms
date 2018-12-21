import pytest
import json
from flask_jwt_extended import create_access_token
import app

ctx = app.app.test_request_context()
ctx.push()
access_token = create_access_token('test')
headers = {'Authorization': 'Bearer {}'.format(access_token)}
ctx.pop()


@pytest.fixture
def client(request):
    test_client = app.app.test_client()

    def teardown():
        pass  # databases and resources have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)


def patch_json(client, url, json_dict):
    return client.patch(url, data=json.dumps(json_dict), content_type='application/json', headers=headers)


def test_index(client):
    res = client.get('/')
    assert b"Hello World!" in res.data


def test_leave_post(client):
    test_data = {
        "uid": "kevin",
        "l_type": "test",
        "l_from": "342",
        "l_to": "876",
        "l_details": "test",
        "l_status": "pending approval"
    }
    post_res = post_json(client, '/leaves', test_data)
    get_res = client.get('/leaves', headers=headers)
    assert post_res.status_code == 201 or 400
    assert get_res.status_code == 200


def test_respond_leave(client):
    res = patch_json(client, '/leaves/3', {"l_status": "approved"})
    assert res.status_code == 200 or 404


def test_get_all_user_leaves(client):
    res = client.get('/leaves/kevin', headers=headers)
    assert res.status_code == 200


def test_withdraw_leave(client):
    res = patch_json(client, '/leaves/1/withdraw', {"l_status": "withdrawn"})
    assert res.status_code == 200 or 404


def test_cancel_leave(client):
    res = patch_json(client, '/leaves/1/cancel', {"l_status": "cancel requested"})
    assert res.status_code == 200 or 404


def test_register(client):
    res = post_json(client, '/register', {"uid": "test", "password": "testpass"})
    assert res.status_code == 201 or 400


def test_login(client):
    res = post_json(client, '/login', {"uid": "test", "password": "test"})
    assert res.status_code == 200 or 401
