from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка на корректный url адрес
        assert 'login' in self.browser.current_url, ' "login" not in URL '

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), ' Login-Form not found '

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), ' Register-Form not found '

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_REG_EMAIL)
        input_email.send_keys(email)

        input_email = self.browser.find_element(*LoginPageLocators.INPUT_REG_PASS1)
        input_email.send_keys(password)

        input_email = self.browser.find_element(*LoginPageLocators.INPUT_REG_PASS2)
        input_email.send_keys(password)

        button_add = self.browser.find_element(*LoginPageLocators.BUTTON_REG)
        button_add.click()



