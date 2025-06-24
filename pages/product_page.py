from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
import time
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_LINK)
        button.click()
        time.sleep(2)

    def is_book_name_correct(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_TITLE).text
        assert book_name == book_title, "The book's name is wrong"

    def is_book_price_correct(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        official_price = self.browser.find_element(*ProductPageLocators.OFFICIAL_PRICE).text
        assert book_price == official_price, "The price is not correct"

    def should_not_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message is presented, but should not be"

    def is_disappeared(self):
        assert not self.is_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message does not disappear"

    def is_not_element_present(self):
        assert not self.is_element_present(*ProductPageLocators.ADD_MESSAGE), \
            "Success message is present"


