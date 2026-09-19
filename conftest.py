import pytest
from selenium import webdriver

from pages import Desk


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1280,900')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def desk(driver):
    return Desk(driver)
