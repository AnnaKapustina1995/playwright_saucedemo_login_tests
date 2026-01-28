import allure


@allure.feature("Авторизация")
@allure.story("Успешный вход")
@allure.title("Пользователь может войти с валидными данными")
def test_login_success(login_page):
    login_page.login("standard_user", "secret_sauce")
    login_page.should_be_logged_in()


@allure.feature("Авторизация")
@allure.story("Неверные данные")
@allure.title("При неверном пароле отображается сообщение об ошибке")
def test_login_wrong_password_shows_error(login_page):
    login_page.login("standard_user", "wrong_password")
    login_page.should_have_error("do not match")


@allure.feature("Авторизация")
@allure.story("Валидация обязательных полей")
@allure.title("При пустых полях отображается сообщение 'Username is required'")
def test_login_empty_fields_shows_required_error(login_page):
    login_page.login_button.click()
    login_page.should_have_error("Username is required")
