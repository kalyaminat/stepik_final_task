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
    # def basket_button_is_active(self):
    #     return WebDriverWait(self.browser, 15).until(EC.element_to_be_clickable(*ProductPageLocators.BUTTON_LINK ))
        #return is_element_present(*ProductPageLocators.BUTTON_LINK)


    def add_product_to_basket(self):

        button = self.browser.find_element(*ProductPageLocators.BUTTON_LINK)
        # button = WebDriverWait(self.browser, 20).until(
        #     EC.element_to_be_clickable(*ProductPageLocators.BUTTON_LINK))
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

