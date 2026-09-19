from data import PASSWORD, USER_NAME
from helpers import generate_email


class TestLogin:
    def test_successful_login_shows_user_in_header(self, desk):
        email = generate_email()
        desk.open_home()
        desk.open_registration()
        desk.register(email, PASSWORD)
        desk.logout()
        desk.open_login()
        desk.login(email, PASSWORD)
        assert desk.user_name() == USER_NAME
        assert desk.is_avatar_displayed() == True
