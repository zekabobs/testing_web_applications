import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON).click()

    def should_be_add_to_cart_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON), "Button 'Add to cart' is not present"

    def should_be_message_success_adding_product(self):
        success_msg = self.browser.find_element(*ProductPageLocators.SUCCESSFUL_ADDING_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(success_msg)
        assert product_name in success_msg, 'Selected product is not current'

    def should_be_correct_coast(self):
        price_from_msg = self.browser.find_element(*ProductPageLocators.CART_COAST_MESSAGE).text
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        print(f'Total coast: {price_from_msg}')
        assert price_product == price_from_msg, f'Prices does not match {price_product} != {price_from_msg}'
