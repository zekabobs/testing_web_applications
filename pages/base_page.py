import math

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), 'Login link is not present'

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_cart_link(self):
        assert self.is_element_present(*BasePageLocators.CART_LINK), 'Cart link is not present'

    def go_to_cart_page(self):
        login_link = self.browser.find_element(*BasePageLocators.CART_LINK)
        login_link.click()

    def is_element_present(self, rule, pattern: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((rule, pattern)))

        except NoSuchElementException:
            return False

        return True

    def is_not_element_present(self, rule, pattern: str, timeout: int = 10) -> bool:
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((rule, pattern)))

        except NoSuchElementException:
            return True
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, rule, pattern: str, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((rule, pattern)))

        except NoSuchElementException:
            return False
        except TimeoutException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")