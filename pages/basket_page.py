from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    """Класс содержит методы для проверок на странице корзины товаров."""

    def should_not_be_product_in_basket(self):
        """Проверяет, что корзина товаров пустая (0 товаров)."""
        assert self.is_not_element_present(*BasketPageLocators.COUNT_PRODUCT_IN_BASKET), 'Basket is not empty'


    def should_be_text_about_basket_empty(self):
        """Проверяет, что на странице корзины товаров есть надпись про пустую корзину."""
        assert 'empty' in  self.get_element_text(*BasketPageLocators.TEXT_BASKET_EMPTY), 'Text about basket empty not found'
