import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(driver):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_success_adding_product()
    product_page.should_be_correct_coast()
