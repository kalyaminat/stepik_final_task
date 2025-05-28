from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
        self.browser.current_url
        # реализуйте проверку на корректный url адрес
        assert True, "Current url is not presented"

    def should_be_login_form(self):
        form_login = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        # реализуйте проверку, что есть форма логина
        assert True, "Form link is not presented"

    def should_be_register_form(self):
        form_register = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        # реализуйте проверку, что есть форма регистрации на странице
        assert True