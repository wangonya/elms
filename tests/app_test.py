from source import app, leaves


def test_index():
    assert app.index() == "Hello World!"


def test_leave_post():
    api_endpoint = app.RequestLeave()
    post_res = api_endpoint.post()
    assert 201 in post_res
