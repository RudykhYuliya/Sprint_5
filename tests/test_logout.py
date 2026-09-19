from data import PASSWORD
from helpers import generate_email


class TestLogout:
    def test_logout_shows_login_button_instead_of_user(self, desk):
        desk.open_home()
        desk.open_registration()
        desk.register(generate_email(), PASSWORD)
        desk.logout()
        assert desk.is_avatar_displayed() == False
        assert desk.is_user_name_displayed() == False
        assert desk.login_button_text() == 'Вход и регистрация'
