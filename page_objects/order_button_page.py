from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class Order_button:
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_SECOND = (By.XPATH, "//button[text()='Заказать']")
    NAME =(By.XPATH, "//input[placeholder='* Имя']")

    def __init__(self,driver):
        self.driver = driver
    
    def first_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(*self.NAME))


    def second_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON_SECOND).click()   
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(*self.NAME))
