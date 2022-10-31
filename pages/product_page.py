from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_add_to_cart_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON), \
            "Button 'Add to cart' is not present"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout=4),  \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout=4), \
            "Success message is not disappeared, but should be"
        
    def should_be_message_success_adding_product(self):
        success_msg = self.browser.find_element(*ProductPageLocators.NAME_FROM_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(success_msg)
        assert product_name == success_msg, 'Selected product is not current'

    def should_be_correct_coast(self):
        price_from_msg = self.browser.find_element(*ProductPageLocators.COAST_FROM_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(f'Total coast: {price_from_msg}')
        assert price_product == price_from_msg, f'Prices does not match {price_product} != {price_from_msg}'
