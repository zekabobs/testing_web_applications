from .pages.product_page import ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
    product_page = ProductPage(driver, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_disappeared_success_message()
