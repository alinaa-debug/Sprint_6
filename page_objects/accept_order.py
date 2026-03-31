from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class accept_page:
    def __init__(self,driver):
        self.driver = driver 

    FORM_ACCEPT_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    ACCEPT_BUTTON = (By.XPATH, "//button[text()='Да']")  
    ORDER_HAS_BEEN = (By.CLASS_NAME ,"Order_Text__2broi")
    
    def accept_order_page(self):
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(self.FORM_ACCEPT_ORDER)
        )
        self.driver.find_element(*self.ACCEPT_BUTTON).click()
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(self.ORDER_HAS_BEEN)
        )
