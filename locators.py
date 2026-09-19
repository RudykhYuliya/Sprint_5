from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Вход и регистрация"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выйти"]')
    PLACE_AD_BUTTON = (By.XPATH, '//button[text()="Разместить объявление"]')
    NO_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Нет аккаунта"]')
    CREATE_ACCOUNT_BUTTON = (By.XPATH, '//button[text()="Создать аккаунт"]')
    SUBMIT_LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    PUBLISH_BUTTON = (By.XPATH, '//button[text()="Опубликовать"]')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    CONFIRM_PASSWORD_INPUT = (By.NAME, 'submitPassword')
    AD_NAME_INPUT = (By.NAME, 'name')
    AD_DESCRIPTION_INPUT = (By.CSS_SELECTOR, 'textarea[name="description"]')
    AD_PRICE_INPUT = (By.NAME, 'price')
    CATEGORY_DROPDOWN_BUTTON = (By.XPATH, '//input[@name="category"]/following-sibling::button')
    CITY_DROPDOWN_BUTTON = (By.XPATH, '//input[@name="city"]/following-sibling::button')
    USED_CONDITION = (By.XPATH, '//label[normalize-space()="Б/У"]')
    AVATAR_BUTTON = (By.CSS_SELECTOR, 'button.circleSmall')
    USER_NAME = (By.CSS_SELECTOR, 'h3.profileText.name')
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        '//input[@name="email"]/following::span[contains(@class,"input_span")][1]',
    )
    EMAIL_ERROR_FIELD = (
        By.XPATH,
        '//input[@name="email"]/ancestor::div[contains(@class,"input_inputError")]',
    )
    PASSWORD_ERROR_FIELD = (
        By.XPATH,
        '//input[@name="password"]/ancestor::div[contains(@class,"input_inputError")]',
    )
    CONFIRM_PASSWORD_ERROR_FIELD = (
        By.XPATH,
        '//input[@name="submitPassword"]/ancestor::div[contains(@class,"input_inputError")]',
    )
    GUEST_MODAL_TITLE = (
        By.XPATH,
        '//h1[text()="Чтобы разместить объявление, авторизуйтесь"]',
    )
    CREATE_AD_TITLE = (By.XPATH, '//h1[text()="Новое объявление"]')
    MY_ADS_HEADING = (By.XPATH, '//h1[text()="Мои объявления"]')

    @staticmethod
    def dropdown_option(option_text):
        return (
            By.XPATH,
            f'//div[contains(@class,"dropDownMenu_options")]//button[normalize-space()="{option_text}"]',
        )

    @staticmethod
    def my_ad_title(title):
        return (
            By.XPATH,
            f'//h1[text()="Мои объявления"]/following::h2[text()="{title}"]',
        )
