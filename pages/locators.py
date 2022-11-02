from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

    REGISTRATION_EMAIL_INPUT = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD1_INPUT = (By.ID, 'id_registration-password1')
    REGISTRATION_PASSWORD2_INPUT = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')

    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')

    NAME_FROM_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    COAST_FROM_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')


class CartPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//*[@id="content_inner"]/p')
    FORM_BASKET = (By.ID, 'basket_formset')
