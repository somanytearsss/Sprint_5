import pytest
from selenium import webdriver
from src.config import Config

@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.maximize_window()
    chrome.get(Config.URL)
    yield chrome
    chrome.quit()