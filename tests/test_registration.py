from data import INVALID_EMAIL, PASSWORD, USER_NAME
from helpers import generate_email


class TestRegistration:
    def test_successful_registration_shows_user_in_header(self, desk):
        desk.open_home()
        desk.open_registration()
        desk.register(generate_email(), PASSWORD)
        assert desk.user_name() == USER_NAME
        assert desk.is_avatar_displayed() == True

    def test_invalid_email_highlights_registration_fields(self, desk):
        desk.open_home()
        desk.open_registration()
        desk.fill_email(INVALID_EMAIL)
        desk.submit_registration()
        assert desk.is_email_highlighted() == True
        assert desk.is_password_highlighted() == True
        assert desk.is_confirm_password_highlighted() == True
        assert desk.email_error_text() == 'Ошибка'

    def test_existing_user_highlights_registration_fields(self, desk):
        email = generate_email()
        desk.open_home()
        desk.open_registration()
        desk.register(email, PASSWORD)
        desk.logout()
        desk.open_registration()
        desk.fill_email(email)
        desk.fill_password(PASSWORD)
        desk.fill_confirm_password(PASSWORD)
        desk.submit_registration()
        assert desk.is_email_highlighted() == True
        assert desk.is_password_highlighted() == True
        assert desk.is_confirm_password_highlighted() == True
        assert desk.email_error_text() == 'Ошибка'
