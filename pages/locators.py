from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_REG_EMAIL = (By.ID, 'id_registration-email')
    INPUT_REG_PASS1 = (By.ID, 'id_registration-password1')
    INPUT_REG_PASS2 = (By.ID, 'id_registration-password2')
    BUTTON_REG = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')

class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main p')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    COUNT_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#content_inner .basket-title')
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')



