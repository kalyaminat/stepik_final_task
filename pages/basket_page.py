from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def is_not_element_present(self):
        assert not self.is_element_present(*BasketPageLocators.GOODS_ADDED), \
            "Success message is present"

    def is_empty_text_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_TEXT), \
            "Basket is not empty"