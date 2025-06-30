import pytest

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_locators.locators import *
from data.data import PersonData
from data.urls import Urls
from web_locators.locator import ButtonEnter, HomePage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Открыть на весь экран
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):

    driver.get(Urls.url_personal_account)

    driver.find_element(*ButtonEnter.be_email_field).send_keys(PersonData.login)
    driver.find_element(*ButtonEnter.be_password_field).send_keys(PersonData.password)
    driver.find_element(*ButtonEnter.be_login_button_any_forms).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located(HomePage.hp_button_order))
    return driver