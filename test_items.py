import time
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestSelenium:

    def test_check_button_add_cart(self, driver):

        driver.get(link)
        time.sleep(30)
        driver.implicitly_wait(5)
        btn = driver.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
        assert btn, "Button 'add to basket' is not exist"
