from .pages.product_page import ProductPage
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from random_word import RandomWords


class TestUserAddToBasketFromProductPage():
    pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser,self.login.link)
        self.login_link = 'https://selenium1py.pythonanywhere.com/ru/accounts/login/'
        r = RandomWords()
        email = r.get_random_word() + "@fakemail.org"
        password = r.get_random_word() + "123"
        self.login_page.open()
        self.login_page.register_new_user()
        self.login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        #page.register_new_user()
        page.add_product_to_basket()
        #page.solve_quiz_and_get_code()
        page.is_book_name_correct()
        page.is_book_price_correct()

    @pytest.mark.need_review
    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.is_not_element_present()



@pytest.mark.parametrize('num', [*range(7), pytest.param(7, marks=pytest.mark.xfail), *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link =  f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.is_book_name_correct()
    page.is_book_price_correct()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.is_not_element_present()
    basket_page.is_empty_text_present()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.is_not_element_present()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_disappeared()









