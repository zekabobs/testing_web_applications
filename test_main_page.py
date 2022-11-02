import pytest

from .pages.main_page import MainPage
from .pages.cart_page import CartPage
from .pages.product_page import ProductPage


@pytest.mark.main_page
def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.should_not_be_products()
    cart_page.should_be_empty_cart_message()


@pytest.mark.main_page
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.should_not_be_products()
    cart_page.should_be_empty_cart_message()
