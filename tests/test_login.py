def test_login_success(login_page):
    login_page.login("standard_user", "secret_sauce")
    login_page.should_be_logged_in()


def test_login_wrong_password_shows_error(login_page):
    login_page.login("standard_user", "wrong_password")
    login_page.should_have_error("do not match")


def test_login_empty_fields_shows_required_error(login_page):
    login_page.login_button.click()
    login_page.should_have_error("Username is required")
