def test_login_success():
    username = "admin"
    password = "1234"
    assert username == "admin"
    assert password == "1234"

def test_login_failure():
    username = "admin"
    password = "salah"
    assert password != "1234"
