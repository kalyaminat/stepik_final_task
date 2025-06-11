from selenium.webdriver.common.by import By

class BasePageLocators():
    url = 'http://selenium1py.pythonanywhere.com/ru/catalogue/'

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_LINK = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ADD_MESSAGE = (By.CSS_SELECTOR, 'div#messages > div:nth-child(1)')
    BOOK_TITLE = (By.CSS_SELECTOR, 'div.col-sm-6 h1')
    BOOK_NAME = (By.CSS_SELECTOR, 'div#messages > :nth-child(1) strong')
    OFFICIAL_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6 > p.price_color')
    BOOK_PRICE =(By.CSS_SELECTOR, 'div#messages > :nth-child(3) strong')