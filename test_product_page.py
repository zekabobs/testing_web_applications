import pytest
from .pages.product_page import ProductPage


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
