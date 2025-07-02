import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import UserData
from src.locators.locators import EnterLocators

from conftest import driver

class TestExitAccount:

    def test_exit_account_by_click_log_out_button_in_personal_cabinet(self, driver):

        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*EnterLocators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.EXIT_BUTTON_IN_PERSONAL_CABINET)))
        driver.find_element(*EnterLocators.EXIT_BUTTON_IN_PERSONAL_CABINET).click()

        WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located(EnterLocators.LOG_IN_BUTTON_REGISTRATION_AND_RECOVERY_FORM))
        assert driver.current_url == f'{Config.URL}/login', 'URL is wrong'