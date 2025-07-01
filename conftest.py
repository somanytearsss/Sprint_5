import pytest
from selenium import webdriver
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from geniration_ep import EmailPasswordGenerator
from data import Credential


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def start_from_login_page(driver):
    login_page = login_site
    driver.get(login_page)

    # Проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_recovery_page(driver):
    login_page = login_site  # Предполагается существование переменной recovery_site
    driver.get(login_page)

    # Кликаем по кнопке "восстановить пароль"
    driver.find_element(*Locators.button_restore_password).click()

    # Ждем загрузку кнопки "войти"
    WebDriverWait(driver, timeout=6).until(
        EC.visibility_of_element_located(Locators.inscription_button_entrance)
    )

    # Кликаем по кнопке "войти"
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver


@pytest.fixture
def start_from_main_page(driver):
    main_page = main_site
    driver.get(main_page)

    # Кликаем по кнопке "Личный кабинет"
    driver.find_element(*Locators.button_personal_area).click()

    # Кликаем по кнопке "Войти" (на форме авторизации)
    driver.find_element(*Locators.button_entrance).click()

    # Заполняем поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_register_page(driver):
    register_page = register_site
    driver.get(register_page)

    # Находим надпись "Войти" и кликаем
    driver.find_element(*Locators.inscription_button_entrance).click()

    # Находим поля и проходим авторизацию
    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def register_new_account(driver):
    login_page = login_site
    driver.get(login_page)

    # Кликаем по надписи "Зарегистрироваться"
    driver.find_element(*Locators.inscription_login).click()

    # Генерация email и password
    generator = EmailPasswordGenerator()
    email, password = generator.generate()

    # Заполняем форму регистрации
    driver.find_element(*Locators.field_name).send_keys(Credential.name)
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)

    # Кликаем на кнопку "Зарегистрироваться"
    driver.find_element(*Locators.button_register).click()

    # Ждем появления кнопки "Войти" (подтверждение успешной регистрации)
    WebDriverWait(driver, timeout=4).until(
        EC.visibility_of_element_located(Locators.button_entrance)
    )

    return driver, email, password