from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time
from selenium.webdriver.common.by import By

# Начало каждой ссылки с товаром по промоакции
link_offer_start = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# Добавление к каждой ссылке порядкового номера от 0 до 9, чтобы сформировать итоговые сслыки
link_offer = [f'{link_offer_start}{i}' for i in range(10)]

# маркировка ссылки ...offer7 как xfail
link_offer[7] = pytest.param(link_offer[7], marks=pytest.mark.xfail)


@pytest.mark.need_review
@pytest.mark.parametrize('link', link_offer)
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тестирует добавление товара в корзину для гостя (с введением промокода).

    Параметр link: список ссылок на товары.
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

def test_guest_should_see_login_link_on_product_page(browser):
    """Тестирует наличие на странице товара ссылки на страницу авторизации для гостя."""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Тестирует переход с главной страницы на страницу авторизации для гостя."""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Тестирует, что гость после добавления товара в корзину не видит сообщения об этом (тест не должен выполняться)."""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.click_add_product_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """Тестирует, что гость не видит сообщения о добавлении товара в корзину, если он его не добавлял."""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """Тестирует, что сообщение о добавлении товара в корзину исчезает через указанное время (тест не должен выполняться)."""
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.click_add_product_button()
    page.should_be_disappeared_success_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Тестирует, что гость не видит товаров в пустой корзине, когда открывает ее со страницы товара."""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_about_basket_empty()


class TestUserAddToBasketFromProductPage():
    """Класс тестов для регистрации пользователя и добавления им товаров в корзину."""

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """Фикстура создает пользователя с заданной почтой и паролем и проверяет корректность входа по иконке логина."""
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email=str(time.time()) + "@myfakemail.org", password='123Qwe#!*789')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Тестирует добавление товара новым пользователем (ссылка с промокодом, т.к. добавление товара реализовано для нее)."""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()

    def test_user_cant_see_success_message(self, browser):
        """Тестирует, что на странице товара нет сообщения о его добавлении, когда новый пользователь его не добавил."""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
