from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.COUNT_PRODUCT_IN_BASKET), 'Basket is not empty'


    def should_be_text_about_basket_empty(self):
        assert 'empty' in  self.get_element_text(*BasketPageLocators.TEXT_BASKET_EMPTY), 'Text about basket empty not found'
