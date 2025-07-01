import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import register_new_account
from geniration_ep import EmailPasswordGenerator
from locators import Locators
from curl import *


@pytest.mark.selenium("register_new_account")
class TestCheckNewRegister:
    driver, email, password = register_new_account
    
