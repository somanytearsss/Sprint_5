from src.config import Config
from src.locators.locators import EnterLocators
from conftest import driver


class TestConstructorSection:

    def test_go_to_the_breads_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.SAUCES_TAB).click()
        driver.find_element(*EnterLocators.BREADS_TAB).click()
        element = driver.find_element(*EnterLocators.CURRENT_BREADS_TAB)
        assert element.is_displayed(), "Another tab is selected"

    def test_go_to_the_sauces_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.SAUCES_TAB).click()
        element = driver.find_element(*EnterLocators.CURRENT_SAUCES_TAB)
        assert element.is_displayed(), "Another tab is selected"


    def test_go_to_the_toppings_section(self, driver):
        driver.get(Config.URL)
        driver.find_element(*EnterLocators.TOPPINGS_TAB).click()
        element = driver.find_element(*EnterLocators.CURRENT_TOPPINGS_TAB)
        assert element.is_displayed(), "Another tab is selected"