from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def is_not_element_present(self):
        assert super().is_not_element_present(
            *BasketPageLocators.GOODS_ADDED,
            timeout=4,
        ), "В корзине присутствует товар"

    def is_empty_text_present(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_TEXT
        ), "Сообщение о пустой корзине отсутствует"