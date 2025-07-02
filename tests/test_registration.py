from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.helpers import Helpers
from src.data import UserData
from src.locators.locators import EnterLocators

from conftest import driver

class TestBurgerRegistration:

    def test_signup(self,driver):
        driver.get(f'{Config.URL}/register')
        email = Helpers.get_random_email()
        password = Helpers.get_random_password()

        name_field = driver.find_element(*EnterLocators.NAME_FIELD)
        name_field.send_keys(UserData.NAME)

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()

        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()

        order_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(EnterLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Button is not displayed"
        assert order_button.is_enabled(), "Button is not enabled"


    def test_an_error_occurs_when_registering_and_entering_an_incorrect_password(self,driver):
        driver.get(f'{Config.URL}/register')

        name_field = driver.find_element(*EnterLocators.NAME_FIELD)
        name_field.send_keys(UserData.NAME)

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.INC_PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()

        error_text = WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(EnterLocators.INCORRECT_PASSWORD))
        assert error_text.is_displayed(), "Error is not displayed"

