from data import AD_CATEGORY, AD_CITY, AD_DESCRIPTION, AD_PRICE, PASSWORD
from helpers import generate_ad_title, generate_email


class TestCreateAdvertisement:
    def test_guest_place_ad_shows_auth_modal(self, desk):
        desk.open_home()
        desk.click_place_ad()
        assert desk.guest_modal_title() == 'Чтобы разместить объявление, авторизуйтесь'

    def test_authorized_user_ad_appears_in_profile(self, desk):
        title = generate_ad_title()
        desk.open_home()
        desk.open_registration()
        desk.register(generate_email(), PASSWORD)
        desk.open_create_ad()
        desk.fill_ad(title, AD_DESCRIPTION, AD_PRICE, AD_CATEGORY, AD_CITY)
        desk.publish_ad()
        desk.open_profile()
        assert desk.my_ad_title(title) == title
