import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from curl import *
from geniration_ep import EmailPasswordGenerator
from locators import Locators
from data import Credential

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_existing_accounts(self, driver):
        # Кликаем по ссылке "Зарегистрироваться"
        driver.find_element(*Locators.inscription_login).click()

        # Заполняем поля формы регистрации
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)

        # Кликаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.button_register).click()

        # Ждем появления ошибки регистрации
        assert WebDriverWait(driver, timeout=5).until(
            EC.visibility_of_element_located(Locators.inscription_error_account)
        )


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckRegistrationNoName:
    def test_registration_no_name(self, driver, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.maximize_window()
        # 1. Кликаем по надписи "Зарегистрироваться"
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(Locators.inscription_login)
        ).click()

        # 2. Генерация тестовых данных (email и пароль)
        generator = EmailPasswordGenerator()
        email, password = generator.generate()

        driver.find_element(*Locators.field_email).send_keys(email)

        driver.find_element(*Locators.field_password).send_keys(password)

        # 4. Кликаем кнопку "Зарегистрироваться"
        driver.find_element(*Locators.button_register).click()

        assert driver.current_url == register_site

