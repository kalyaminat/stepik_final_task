from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(ProductPageLocators.BUTTON_LINK)
        )
        button.click()

    def is_book_name_correct(self):
        book_name = WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(ProductPageLocators.BOOK_NAME)
        ).text
        book_title = WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(ProductPageLocators.BOOK_TITLE)
        ).text

        assert book_name == book_title, (
            f"Название в сообщении: {book_name!r}; "
            f"название товара: {book_title!r}"
        )

    def is_book_price_correct(self):
        book_price = WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(ProductPageLocators.BOOK_PRICE)
        ).text
        official_price = WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(
                ProductPageLocators.OFFICIAL_PRICE
            )
        ).text

        assert book_price == official_price, (
            f"Сумма в сообщении: {book_price!r}; "
            f"цена товара: {official_price!r}"
        )

    def should_not_be_success_message(self):
        assert super().is_not_element_present(
            *ProductPageLocators.ADD_MESSAGE,
            timeout=4,
        ), "Сообщение об успешном добавлении присутствует"

    def is_disappeared(self):
        assert super().is_disappeared(
            *ProductPageLocators.ADD_MESSAGE,
            timeout=4,
        ), "Сообщение об успешном добавлении не исчезло"

    def is_not_element_present(self):
        self.should_not_be_success_message()