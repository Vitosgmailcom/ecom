import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="class")
def init_driver(request):
    supported_browser = ['chrome', 'ch', 'headless', 'firefox', 'ff']
    browser = os.environ.get("BROWSER", None)
    browser = browser.lower()
    if not browser:
        raise Exception(f"The browser must be set.")

    if browser not in supported_browser:
        raise Exception(f"The set browser '{browser}' is not supported. "
                        f"Please use one of the supported browsers: '{supported_browser}'")

    if browser in ('chrome', 'ch'):
        driver = webdriver.Chrome()

    elif browser in ('firefox', 'ff'):
        driver = webdriver.Firefox()


    request.cls.driver = driver
    yield
    driver.quit()







