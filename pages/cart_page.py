from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(CartPage, self).__init__(*args, **kwargs)

    def should_not_be_products(self):
        assert self.is_not_element_present(*CartPageLocators.FORM_BASKET), \
            'Products are present, but should not be'

    def should_be_empty_cart_message(self):
        if not self.is_element_present(*CartPageLocators.EMPTY_BASKET_MESSAGE):
            assert False, 'Empty cart message in not present'
        msg = self.browser.find_element(*CartPageLocators.EMPTY_BASKET_MESSAGE).text

        # Work only on english
        if not 'empty' in msg:
            assert False, 'Message is present, but not empty'
