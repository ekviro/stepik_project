from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import time


class BasePage():
    """Класс содержит методы, общие для любых страниц сайта."""

    def __init__(self, browser, url, timeout=10):
        """Устанавливает драйвер браузера, ссылку на сайт и время ожидания каждого элемента страницы."""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def get_element_text(self, how, what):
        """
        Возвращает текст элемента страницы.

        Аргументы: how, what - тип локатора и значение локатора для поиска элемента. Например: (By.CSS_SELECTOR, "#login_link").

        Возвращает: текст элемента, найденного по указанному локатору.
        """
        if self.is_element_present(how, what):
            return self.browser.find_element(how, what).text


    def is_not_element_present(self, how, what, timeout=4):
        """
        Проверяет, что элемент не появляется в течение заданного времени.

        Аргументы:
        how, what: тип локатора и значение локатора для поиска элемента. Например: (By.CSS_SELECTOR, "#login_link").
        timeout: время ожидания в секундах.

        Возвращает:
        Истина: Если элемент не появляется на странице в течение заданного времени.
        Ложь: Если элемент появился до истечения времени
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False


    def is_element_present(self, how, what):
        """
        Проверяет, что элемент существует на странице.

        Аргументы: how, what - тип локатора и значение локатора для поиска элемента. Например: (By.CSS_SELECTOR, "#login_link").

        Возвращает:
        Истина: Если элемент найден.
        Ложь: Если не найден элемент по локатору (перехватывает исключение NoSuchElementException).
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True


    def is_disappeared(self, how, what, timeout=4):
        """
        Проверяет исчезновение элемента со страницы через заданное время.

        Аргументы:
        how, what: тип локатора и значение локатора для поиска элемента. Например: (By.CSS_SELECTOR, "#login_link").
        timeout: время ожидания в секундах.

        Возвращает:
        Истина: Если элемент исчез со страницы до истечения заданного времени.
        Ложь: Если элемент остался на странице через заданное время
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        """Переходит на страницу авторизации."""
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_basket(self):
        """Переходит на страницу корзины товаров."""
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_login_link(self):
        """Проверяет наличие ссылки авторизации."""
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def open(self):
        """Открывает страницу в браузере по ссылке текущего объекта (была задана при создании)."""
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        """Вводит значения во всплывающие окна для тестов с промоакциями."""
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_authorized_user(self):
        """Проверяет наличие иконки пользователя как признак успешной авторизации"""
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"



