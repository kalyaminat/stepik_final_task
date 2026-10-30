from urllib.parse import urlparse

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        path = urlparse(self.browser.current_url).path
        assert path.rstrip("/").endswith("/accounts/login"), (
            f"Открыта не страница входа: {self.browser.current_url}"
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            "Форма входа отсутствует"
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            "Форма регистрации отсутствует"
        )

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REMAIL
        ).send_keys(email)

        self.browser.find_element(
            *LoginPageLocators.RPASSWORD
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.RPASSWORD2
        ).send_keys(password)

        self.browser.find_element(
            *LoginPageLocators.RBUTTON
        ).click()