from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group')
    LOGIN_URL = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
    USER_ICON = (By.CSS_SELECTOR, 'i.icon-user')

class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    RPASSWORD = (By.CSS_SELECTOR, '#id_registration-password')
    RPASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    RBUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    PASSWORD = (By.CSS_SELECTOR, '#id_login-password')
    BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")
    NAVBAR = (By.CSS_SELECTOR, '.nav.navbar-nav.navbar-right')

class ProductPageLocators():
    BUTTON_LINK = (By.CSS_SELECTOR,'button.btn-add-to-basket')
    BOOK_TITLE = (By.CSS_SELECTOR, 'div.col-sm-6 > h1')
    ADD_MESSAGE = (By.CSS_SELECTOR, 'div#messages > div:nth-child(1)')
    BOOK_NAME = (By.CSS_SELECTOR, 'div#messages > :nth-child(1) strong')
    OFFICIAL_PRICE = (By.CSS_SELECTOR, 'div.col-sm-6 > p.price_color')
    BOOK_PRICE =(By.CSS_SELECTOR, 'div#messages > :nth-child(3) strong')

class BasketPageLocators():
    GOODS_ADDED = (By.CSS_SELECTOR, 'div.checkout-quantity ')
    EMPTY_TEXT = (By.XPATH, "//p[contains(text(), 'empty')]")
