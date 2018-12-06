from source import app


def test_index():
    assert app.index() == "Hello World!"


def test_leave_post():
    api_endpoint = app.RequestLeave()
    post_res = api_endpoint.post()
    get_res = api_endpoint.get()
    assert 201 in post_res and 200 in get_res


def test_respond_leave():
    api_endpoint = app.RespondToRequests()
    get_res = api_endpoint.patch(leave_id=3)
    assert 200 in get_res


def test_get_all_user_leaves():
    api_endpoint = app.GetAllUserLeaves()
    get_res = api_endpoint.get(uid='test')
    assert 200 in get_res


def test_get_user_leave_history():
    api_endpoint = app.GetUserLeaveHistory()
    get_res = api_endpoint.get(uid='test')
    assert 200 in get_res


def test_withdraw_leave():
    api_endpoint = app.WithdrawLeave()
    get_res = api_endpoint.patch(uid='test', leave_id=3)
    assert 200 in get_res


def test_cancel_leave():
    api_endpoint = app.CancelLeave()
    get_res = api_endpoint.patch(uid='test', leave_id=7)
    assert 200 in get_res
