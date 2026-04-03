
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from locators.accept_order_locators import AcceptOrderLocators
from page_objects.base_page import BasePage

class AcceptPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    def accept_order_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(AcceptOrderLocators.FORM_ACCEPT_ORDER)
        )
        
        self.driver.find_element(*AcceptOrderLocators.ACCEPT_BUTTON).click()
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(AcceptOrderLocators.ORDER_HAS_BEEN)
        )
