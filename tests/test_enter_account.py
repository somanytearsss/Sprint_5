from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import UserData
from src.locators.locators import EnterLocators

from conftest import driver

class TestBurgerEnterAccount:

    def test_enter_account(self,driver):
        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()

        order_button = WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(EnterLocators.ORDER_BUTTON))
        assert order_button.is_displayed(), "Button is not displayed"
        assert order_button.is_enabled(), "Button is not enabled"

    def test_log_in_using_the_Log_in_account_button_on_the_main_page(self,driver):
        driver.get(Config.URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.ENTER_MAIN)))
        driver.find_element(*EnterLocators.ENTER_MAIN).click()
        assert  driver.current_url == f'{Config.URL}/login', 'URL is wrong'

    def test_log_in_personal_account_on_header(self,driver):
        driver.get(Config.URL)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.ENTER_MAIN)))
        driver.find_element(*EnterLocators.PERSONAL_ACCOUNT_BUTTON).click()
        assert  driver.current_url == f'{Config.URL}/login', 'URL is wrong'

    def test_log_in_the_button_in_the_registration_form(self,driver):
        driver.get(f'{Config.URL}/register')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM)))
        driver.find_element(*EnterLocators.LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM).click()
        assert  driver.current_url == f'{Config.URL}/login', 'URL is wrong'

    def test_log_in_the_button_in_the_recovery_form(self,driver):
        driver.get(f'{Config.URL}/forgot-password')
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM)))
        driver.find_element(*EnterLocators.LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM).click()
        assert  driver.current_url == f'{Config.URL}/login', 'URL is wrong'