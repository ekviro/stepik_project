from selenium.webdriver.common.by import By


class MainPageLocators():
    """Локаторы для поиска элементов на главной странице сайта."""
    pass

class LoginPageLocators():
    """
    Локаторы для поиска элементов на странице авторизации.

    LOGIN_FORM: форма входа для зарегистрированнного пользователя
    REGISTER_FORM: форма регистрации нового пользователя
    INPUT_REG_EMAIL: поле ввода почтового ящика при регистрации нового пользователя
    INPUT_REG_PASS1: поле ввода пароля при регистрации нового пользователя
    INPUT_REG_PASS2: поле подтверждения пароля при регистрации нового пользователя
    BUTTON_REG: кнопка сохранения данных при регистрации нового пользователя
    """

    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    INPUT_REG_EMAIL = (By.ID, 'id_registration-email')
    INPUT_REG_PASS1 = (By.ID, 'id_registration-password1')
    INPUT_REG_PASS2 = (By.ID, 'id_registration-password2')
    BUTTON_REG = (By.CSS_SELECTOR, 'button[name = "registration_submit"]')

class ProductPageLocators():
    """
    Локаторы для поиска элементов на странице отдельного товара.

    PRODUCT_NAME: название товара на странице товара
    PRODUCT_PRICE: цена товара на странице товара
    BUTTON_ADD_TO_BASKET: кнопка добавления товара в корзину
    NAME_IN_BASKET: название товара в корзине
    PRICE_IN_BASKET: цена товара в корзине
    SUCCESS_MESSAGE: сообщение о добавлении товара в корзину
    """

    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main p')
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner')

class BasePageLocators():
    """
    Локаторы для поиска элементов на странице корзины товаров.

    LOGIN_LINK: ссылка на страницу авторизации
    LOGIN_LINK_INVALID: пример некорректной сслыки на страницу авторизации
    BASKET_LINK: ссылка на страницу корзины товаров
    USER_ICON: иконка авторизованного пользователя после логина
    """
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    """
    Локаторы для поиска элементов на странице корзины товаров.

    COUNT_PRODUCT_IN_BASKET: количество товаров в корзине.
    TEXT_BASKET_EMPTY: элемент, где содержится текст о пустой корзине
    """
    COUNT_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#content_inner .basket-title')
    TEXT_BASKET_EMPTY = (By.CSS_SELECTOR, '#content_inner p')
