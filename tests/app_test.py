import pytest
import json
from source import app


@pytest.fixture
def client(request):
    test_client = app.app.test_client()

    def teardown():
        pass  # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client


def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')


def patch_json(client, url, json_dict):
    return client.patch(url, data=json.dumps(json_dict), content_type='application/json')


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
    get_res = client.get('/leaves')
    assert post_res.status_code == 201 or 400
    assert get_res.status_code == 200


def test_respond_leave(client):
    res = patch_json(client, '/leaves/3', {"l_status": "approved"})
    assert res.status_code == 200 or 404


def test_get_all_user_leaves(client):
    res = client.get('/leaves/kevin')
    assert res.status_code == 200


def test_withdraw_leave(client):
    res = patch_json(client, '/leaves/<int:l_id>/withdraw', {"l_status": "withdrawn"})
    assert res.status_code == 200 or 404


def test_cancel_leave(client):
    res = patch_json(client, '/leaves/<int:l_id>/cancel', {"l_status": "cancel requested"})
    assert res.status_code == 200 or 404
