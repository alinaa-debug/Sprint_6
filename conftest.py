import pytest
from selenium import webdriver 
from data import Urls

@pytest.fixture(scope=function)
def driver():
    driver = webdriver.Chrome()
    driver.get(Urls.BASE_URL)
    yield driver

    driver.quit()

@pytest.fixture(scope=function)
def driver2():
    driver = webdriver.Firefox()
    driver.get(Urls.ORDER_URL)
    yield driver

    driver.quit()
