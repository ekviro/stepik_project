from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    """Класс содержит методы для страницы отдельного товара."""

    def click_add_product_button(self):
        """Нажимает на кнопку добавления товара в корзину."""
        self.should_see_add_to_basket_button()
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()

    def add_product_to_basket(self):
        """Добавляет товар в корзину, вводит промокод во всплывающем окне, проверяет название и цену товара."""
        self.click_add_product_button()
        self.solve_quiz_and_get_code()

        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        name_in_basket = self.get_element_text(*ProductPageLocators.NAME_IN_BASKET)
        self.should_be_correct_product_name_in_basket(name, name_in_basket)

        price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        self.should_be_correct_product_price_in_basket(price, price_in_basket)

    def should_see_add_to_basket_button(self):
        """Проверяет наличие кнопки добавления товара."""
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), ' Button "Add to basket" not found '

    def should_see_product_name(self):
        """Проверяет наличие названия товара на странице товара."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ' Product name not found '

    def should_see_product_name_in_basket(self):
        """Проверяет наличие названия товара в корзине."""
        assert self.is_element_present(*ProductPageLocators.NAME_IN_BASKET), ' Product name in basket not found '

    def should_be_correct_product_name_in_basket(self, name, name_in_basket):
        """Проверяет, что название товара в корзине совпадает с названием выбранного товара."""
        self.should_see_product_name()
        self.should_see_product_name_in_basket()
        assert name == name_in_basket, ' name and name in basket is different '

    def should_see_product_price(self):
        """Проверяет наличие цены товара на странице товара."""
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ' Product price not found '

    def should_see_product_price_in_basket(self):
        """Проверяет наличие цены товара в корзине."""
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), ' Product price in basket not found '

    def should_be_correct_product_price_in_basket(self, price, price_in_basket):
        """Проверяет, что цена товара в корзине совпадает с ценой выбранного товара."""
        self.should_see_product_price()
        self.should_see_product_price_in_basket()
        assert price == price_in_basket, ' price and price in basket is different '

    def should_not_be_success_message(self):
        """Проверяет, что нет сообщения о добавлении товара в корзину."""
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        """Проверяет, что сообщение о добавлении товара исчезло через заданное время."""
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message did not disappear after the specified time'
