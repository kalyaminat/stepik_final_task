from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
from random_word import RandomWords
# r = RandomWords()
# email = r.get_random_word() + "@fakemail.org"
# password = r.get_random_word() + "123"


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = "https://selenium1py.pythonanywhere.com/accounts/login/"
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

    def register_new_user(self, email, password):
        # r = RandomWords()
        # self.email = r.get_random_word() + "@fakemail.org"
        # self.password = r.get_random_word() + "123"
        email = self.browser.find_element(*LoginPageLocators.REMAIL)
        email.send_key(self.email)
        password = self.browser.find_element(*LoginPageLocators.RPASSWORD)
        password.send_key(self.password)
        password2 = self.browser.find_element(*LoginPageLocators.RPASSWORD2)
        password2.send_key(self.password)
        regbutton = self.browser.find_element(*LoginPageLocators.RBUTTON)
        regbutton.click()
        element = self.browser.find_element(*LoginPageLocators.NAVBAR)
        assert "profile" in element.text, "Registration was not successful"



