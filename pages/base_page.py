import math

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.browser.implicitly_wait(0)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = WebDriverWait(self.browser, self.timeout).until(
            EC.alert_is_present()
        )
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()

        try:
            second_alert = WebDriverWait(self.browser, 3).until(
                EC.alert_is_present()
            )
        except TimeoutException:
            return

        print(f"Your code: {second_alert.text}")
        second_alert.accept()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(BasePageLocators.LOGIN_LINK)
        )
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Ссылка на вход отсутствует"

    def go_to_basket_page(self):
        link = WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(BasePageLocators.BASKET_LINK)
        )
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "Значок пользователя отсутствует: авторизация не подтверждена"