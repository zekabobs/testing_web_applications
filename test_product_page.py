import time
import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.cart_page import CartPage


@pytest.mark.user_test
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        email = str(time.time()) + "@fakemail.org"
        self.link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
        self.login_page = LoginPage(driver, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        self.login_page.open()
        self.login_page.register_new_user(email, password=email)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, driver):
        product_page = ProductPage(driver, self.link)
        product_page.open()
        product_page.add_to_cart()
        product_page.should_be_message_success_adding_product()
        product_page.should_be_correct_coast()

    def test_user_can_add_product_to_basket(self, driver):
        product_page = ProductPage(driver, self.link)
        product_page.open()
        product_page.add_to_cart()


@pytest.mark.need_review
def test_user_can_add_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_cart()


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    *[
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer' +
        str(num) for num in range(10) if num != 7]
    ,
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                 marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_cart(driver, link):
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_message_success_adding_product()
    product_page.should_be_correct_coast()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.go_to_cart_page()
    cart_page = CartPage(driver, driver.current_url)
    cart_page.should_not_be_products()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()
