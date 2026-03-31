from selenium.webdriver.common.by import By
from locators import SAMOKAT_BUTTON, YANDEX_BUTTON

class samokat_button_page:
    def __init__(self,driver):
        self.driver = driver


    def click_samocat_button(self):
        self.driver.find_element(*SAMOKAT_BUTTON).click()
        


    def click_yandex_button_page(self):
        self.driver.find_element(*YANDEX_BUTTON).click()

