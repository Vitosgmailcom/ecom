 ### conftest.py setting ###

@pytest.fixture(scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()
 -----------------------------------------------------   
    
  ###  calling fixture in the test file ###
import pytest
import pdb

@pytest.mark.usefixtures("init_driver")
class TestDummy():
    def test_dummy_func(self):
        print("Hello")
 -----------------------------------------------------       
 ### config_helper.py ### 
 
 
import os

def base_url():

    env = os.environ.get('ENV', 'test')

    if env.lower() == 'test':
        return "http://ask-stage.portnov.com/#"
    elif env.lower() == 'prod':
        return "http://ask-stage.production.portnov.com/"
    else
        raise Exception(f" Unknown environment: {env}")
-------------------------------------------------------