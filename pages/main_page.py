from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .product_page import ProductPage


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


    # def go_to_product_page(self):
    #     product_link = 'https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    #     link = self.browser.get(product_link)
    #     product_link.click()
    #     return ProductPage(browser=self.browser, url=self.browser.current_url)
    #     alert = self.browser.switch_to.alert
    #     alert.accept()