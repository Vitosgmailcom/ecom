import time

from ecom_test.src.SeleniumExtended import SeleniumExtended
from ecom_test.src.pages.locators.locators import LogonPageLocators

class LoginPage(LogonPageLocators):


    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_login_page(self):
        self.driver.get("http://ask-stage.portnov.com/#/login")

    def input_user_name(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    # pdb.set_trace()
    def input_user_pasw(self, passsword):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, passsword)

    def click_login_btn(self):
        self.sl.wait_and_click(self.LOGIN_BUTTON)

    def sleep_(self, timeout):
        time.sleep(timeout)

