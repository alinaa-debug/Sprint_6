from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_buttons_locator import OrderButton
from page_objects.base_page import BasePage
from locators.for_who_samokat_locators import ForWhoSamokatLocator
from selenium.webdriver.common.by import By

class Order_button(BasePage):
    
    def __init__(self,driver):
        super().__init__(driver)
    COOKIE = [By.XPATH, "//button[contains(text(),'да все привыкли')]"]
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.COOKIE)
        ).click()
        except:
            pass
    
    def first_order_button(self):
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(OrderButton.ORDER_BUTTON)
        )
        self.driver.find_element(*OrderButton.ORDER_BUTTON).click()
    
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.NAME))
        


    def second_order_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*OrderButton.ORDER_BUTTON_SECOND).click() 
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.NAME))
