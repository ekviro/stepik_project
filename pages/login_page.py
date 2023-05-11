from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """Класс содержит методы для страницы авторизации."""


    def should_be_login_page(self):
        """Проверяет, что это страница авторизации с помощью трех проверок-методов."""
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет, что текущий url-адрес содержит слово 'login'."""
        assert 'login' in self.browser.current_url, ' "login" not in URL '

    def should_be_login_form(self):
        """Проверяет, что на странице есть форма авторизации для зарегистрированных пользователей."""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), ' Login-Form not found '

    def should_be_register_form(self):
        """Проверяет, что на странице есть форма регистрации нового пользователя."""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), ' Register-Form not found '

    def register_new_user(self, email, password):
        """
        Регистрирует нового пользователя.


        Аргументы:
        email: почтовый ящик
        password: пароль и повторный пароль для подтверждения (требуется сложный пароль не менее 9 символов).
        """
        input_data = self.browser.find_element(*LoginPageLocators.INPUT_REG_EMAIL)
        input_data.send_keys(email)

        input_data = self.browser.find_element(*LoginPageLocators.INPUT_REG_PASS1)
        input_data.send_keys(password)

        input_data = self.browser.find_element(*LoginPageLocators.INPUT_REG_PASS2)
        input_data.send_keys(password)

        button_add = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button_add.click()
