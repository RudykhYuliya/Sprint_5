from selenium.common.exceptions import InvalidElementStateException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import BASE_URL
from locators import Locators


class Desk:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def _click(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def _set_value(self, locator, text):
        def typed(driver):
            try:
                field = driver.find_element(*locator)
                driver.execute_script('arguments[0].scrollIntoView({block: "center"});', field)
                field = driver.find_element(*locator)
                try:
                    field.click()
                    field.clear()
                except InvalidElementStateException:
                    pass
                field.send_keys(text)
                return True
            except (InvalidElementStateException, StaleElementReferenceException):
                return False

        self.wait.until(typed)

    def open_home(self):
        self.driver.get(BASE_URL)

    def open_login(self):
        self.wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))

    def open_registration(self):
        self.open_login()
        self.wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(Locators.CONFIRM_PASSWORD_INPUT))

    def fill_email(self, email):
        self._set_value(Locators.EMAIL_INPUT, email)

    def fill_password(self, password):
        self._set_value(Locators.PASSWORD_INPUT, password)

    def fill_confirm_password(self, password):
        self._set_value(Locators.CONFIRM_PASSWORD_INPUT, password)

    def submit_registration(self):
        self.wait.until(EC.element_to_be_clickable(Locators.CREATE_ACCOUNT_BUTTON)).click()

    def submit_login(self):
        self.wait.until(EC.element_to_be_clickable(Locators.SUBMIT_LOGIN_BUTTON)).click()

    def register(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.fill_confirm_password(password)
        self.submit_registration()
        self.wait.until(EC.visibility_of_element_located(Locators.USER_NAME))

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.submit_login()
        self.wait.until(EC.visibility_of_element_located(Locators.USER_NAME))

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))

    def user_name(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.USER_NAME)).text

    def is_avatar_displayed(self):
        return len(self.driver.find_elements(*Locators.AVATAR_BUTTON)) > 0

    def is_user_name_displayed(self):
        return len(self.driver.find_elements(*Locators.USER_NAME)) > 0

    def login_button_text(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON)).text

    def email_error_text(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MESSAGE)).text

    def is_email_highlighted(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_FIELD)).is_displayed()

    def is_password_highlighted(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.PASSWORD_ERROR_FIELD)).is_displayed()

    def is_confirm_password_highlighted(self):
        return self.wait.until(
            EC.visibility_of_element_located(Locators.CONFIRM_PASSWORD_ERROR_FIELD)
        ).is_displayed()

    def click_place_ad(self):
        self.wait.until(EC.element_to_be_clickable(Locators.PLACE_AD_BUTTON)).click()

    def guest_modal_title(self):
        return self.wait.until(EC.visibility_of_element_located(Locators.GUEST_MODAL_TITLE)).text

    def open_create_ad(self):
        self.click_place_ad()
        self.wait.until(EC.visibility_of_element_located(Locators.CREATE_AD_TITLE))

    def fill_ad(self, title, description, price, category, city):
        self._set_value(Locators.AD_NAME_INPUT, title)
        self._click(Locators.CATEGORY_DROPDOWN_BUTTON)
        self._click(Locators.dropdown_option(category))
        self._click(Locators.CITY_DROPDOWN_BUTTON)
        self._click(Locators.dropdown_option(city))
        self._click(Locators.AD_NAME_INPUT)
        self._set_value(Locators.AD_DESCRIPTION_INPUT, description)
        self._set_value(Locators.AD_PRICE_INPUT, price)
        self._click(Locators.USED_CONDITION)

    def publish_ad(self):
        self._click(Locators.PUBLISH_BUTTON)
        self.wait.until(lambda driver: 'create-lisiting' not in driver.current_url)

    def open_profile(self):
        self.wait.until(EC.element_to_be_clickable(Locators.AVATAR_BUTTON)).click()
        self.wait.until(EC.url_contains('profile'))
        self.wait.until(EC.visibility_of_element_located(Locators.MY_ADS_HEADING))

    def my_ad_title(self, title):
        return self.wait.until(EC.visibility_of_element_located(Locators.my_ad_title(title))).text
