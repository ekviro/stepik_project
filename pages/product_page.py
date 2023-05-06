import time
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_see_add_to_basket_button()
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()
        self.solve_quiz_and_get_code()
        self.should_be_correct_product_name_in_basket()
        self.should_be_correct_product_price_in_basket()

    def should_see_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), ' Button "Add to basket" not found '

    def should_see_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ' Product name not found '

    def should_see_product_name_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_IN_BASKET), ' Product name in basket not found '

    def should_be_correct_product_name_in_basket(self):
        self.should_see_product_name()
        self.should_see_product_name_in_basket()
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        name_in_basket = self.browser.find_element(*ProductPageLocators.NAME_IN_BASKET).text
        assert name == name_in_basket, ' name and name in basket is different '

    def should_see_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ' Product price not found '

    def should_see_product_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), ' Product price in basket not found '


    def should_be_correct_product_price_in_basket(self):
        self.should_see_product_price()
        self.should_see_product_price_in_basket()
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == price_in_basket, ' price and price in basket is different '
