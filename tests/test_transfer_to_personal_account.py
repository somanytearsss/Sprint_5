from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.config import Config
from src.data import UserData
from src.locators.locators import EnterLocators

from conftest import driver

class TestBurgerTransferToPersonalAccount:

    def test_the_click_through_personal_account_on_header(self,driver):
        driver.get(f'{Config.URL}/login')

        email_field = driver.find_element(*EnterLocators.EMAIL_FIELD)
        email_field.send_keys(UserData.EMAIL)

        password_field = driver.find_element(*EnterLocators.PASSWORD_FIELD)
        password_field.send_keys(UserData.PASSWORD)

        driver.find_element(*EnterLocators.ENTER_MAIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.ORDER_BUTTON)))

        driver.find_element(*EnterLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((EnterLocators.EXIT_BUTTON_IN_PERSONAL_CABINET)))
        assert  driver.current_url == f'{Config.URL}/account/profile', 'URL is wrong'