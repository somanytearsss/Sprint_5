import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import register_new_account
from data import Credential
from geniration_ep import EmailPasswordGenerator
from locators import Locators
from curl import *


@pytest.mark.usefixtures("register_new_account")
class TestCheckNewRegister:
    def test_registration(self):
        driver, email, password = register_new_account

    # Находим поле "email" и заполняем его
    driver.find_element(*Locators.field_email).send_keys(email)

    # Находим поле "Пароль" и заполняем его
    driver.find_element(*Locators.field_password).send_keys(password)

    # Кликаем по кнопке "Войти"
    driver.find_element(*Locators.button_entrance).click()

    # Ждем перехода на главную страницу
    WebDriverWait(driver, timeout=10).until(
        EC.url_to_be(main_site)
    )

    # Проверяем успешную авторизацию
    assert driver.current_url == main_site
