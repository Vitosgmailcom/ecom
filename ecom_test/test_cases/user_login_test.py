import pytest
from ecom_test.src.pages.login_page_objects import LoginPage

@pytest.mark.usefixtures("init_driver")

class TestLogin:
    username = "vitaly.kamynin@gmail.com"
    password = "Fall2020!"

    @pytest.mark.id1
    def test_login_existing_user(self):
        existing_user = LoginPage(self.driver)
        existing_user.go_to_login_page()
        existing_user.input_user_name(self.username)
        existing_user.input_user_pasw(self.password)
        existing_user.click_login_btn()
        existing_user.sleep_(10)

    @pytest.mark.id2
    def test_login_negative(self):
        non_existing_user = LoginPage(self.driver)
        non_existing_user.go_to_login_page()
        non_existing_user.input_user_name("qweqwe")
        non_existing_user.input_user_pasw("qeqweqew")
        non_existing_user.click_login_btn()

