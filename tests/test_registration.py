import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
from locators import Locators
from data import Credential

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_existing_accounts(self, driver, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()

        # Кликаем по ссылке "Зарегистрироваться"
        driver.find_element(*Locators.inscription_login).click()

        # Заполняем поле "Имя"
        driver.find_element(*Locators.field_name).send_keys(Credential.name)

        # Заполняем поле "Email"
        driver.find_element(*Locators.field_email).send_keys(Credential.email)

        # Заполняем поле "Пароль"
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # Кликаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.button_register).click()

        assert WebDriverWait(driver, timeout=5).until(EC.visibility_of_element_located(Locators.inscription_error_account))