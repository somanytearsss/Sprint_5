from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import UserData
from src.locators.locators import EnterLocators

from conftest import driver

class TestBurgerSwitchPersonalAccountToConstructor:

    def test_the_click_to_constructor_on_header_and_switch_personal_account_to_constructor(self,driver):
        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.ORDER_BUTTON)))

        driver.find_element(*EnterLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.CONSTRUCTOR_HEADER)))
        driver.find_element(*EnterLocators.CONSTRUCTOR_HEADER).click()

        assert  driver.current_url == f'{Config.URL}/', 'URL is wrong'

    def test_the_click_to_stellar_burger_on_header_and_switch_personal_account_to_constructor(self,driver):
        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.ORDER_BUTTON)))

        driver.find_element(*EnterLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.STELLAR_BURGER_HEADER)))
        driver.find_element(*EnterLocators.STELLAR_BURGER_HEADER).click()

        assert  driver.current_url == f'{Config.URL}/', 'URL is wrong'