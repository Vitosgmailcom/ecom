from selenium.webdriver.common.by import By


class LogonPageLocators:

    LOGIN_USER_NAME = (By.XPATH, '//input[@formcontrolname="email"]')
    LOGIN_PASSWORD = (By.XPATH, '//input[@formcontrolname="password"]')
    LOGIN_BUTTON = (By.XPATH, '//span[contains(text(),"Sign In")]')




