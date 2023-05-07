from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_product_button(self):
        self.should_see_add_to_basket_button()
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add.click()

    def add_product_to_basket(self):
        self.click_add_product_button()
        self.solve_quiz_and_get_code()

        name = self.get_element_text(*ProductPageLocators.PRODUCT_NAME)
        name_in_basket = self.get_element_text(*ProductPageLocators.NAME_IN_BASKET)
        self.should_be_correct_product_name_in_basket(name, name_in_basket)

        price = self.get_element_text(*ProductPageLocators.PRODUCT_PRICE)
        price_in_basket = self.get_element_text(*ProductPageLocators.PRICE_IN_BASKET)
        self.should_be_correct_product_price_in_basket(price, price_in_basket)

    def should_see_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), ' Button "Add to basket" not found '

    def should_see_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), ' Product name not found '

    def should_see_product_name_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.NAME_IN_BASKET), ' Product name in basket not found '

    def should_be_correct_product_name_in_basket(self, name, name_in_basket):
        self.should_see_product_name()
        self.should_see_product_name_in_basket()
        assert name == name_in_basket, ' name and name in basket is different '

    def should_see_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), ' Product price not found '

    def should_see_product_price_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), ' Product price in basket not found '


    def should_be_correct_product_price_in_basket(self, price, price_in_basket):
        self.should_see_product_price()
        self.should_see_product_price_in_basket()
        assert price == price_in_basket, ' price and price in basket is different '

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            'Success message did not disappear after the specified time'
