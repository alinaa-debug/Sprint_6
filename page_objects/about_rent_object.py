from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class SamokatPage:
    def __init__(self,driver):
        self.driver = driver 


    DELEVIRY_INPUT = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
    DATE1 = (By.XPATH, "//div[text()= '20']")
    DATE2 = (By.XPATH, "//div[text()= '18']")
    RENTAL_PERIOD = (By.XPATH, "//div[text()='* Срок аренды']")
    FIRST_PERIOD = (By. XPATH, "//div[text()= 'двое суток']")
    SECOND_PERIOD = (By. XPATH, "//div[text()= 'сутки']")
    BLACK = (By.ID, "black")
    GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder= 'Комментарий для курьера']")
    FOR_ORDER_BUTTON = (By.XPATH, "//button[text()= 'Заказать']")
    SUCCESSFUL_ORDER = (By.CLASS_NAME, 'Order_Text__2broi')
    FORM_ACCEPT_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')

    def about_rent_first(self):
        webdriver.wait(self.driver,5).until(
        EC.visibility_of_element_located(self.DELEVIRY_INPUT)
        )
        self.driver.find_element(*self.DELEVIRY_INPUT).click()
        self.driver.find_element(*self.DATE1).click()
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        self.driver.find_element(*self.FIRST_PERIOD).click()
        self.driver.find_element(*self.BLACK).click()
        self.driver.find_element(*self.COMMENT).click()
        self.driver.find_element(*self.FOR_ORDER_BUTTON).click()
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(self.FORM_ACCEPT_ORDER)
        )

    def about_rent_second(self):
        webdriver.wait(self.driver,5).until(
        EC.visibility_of_element_located(self.DELEVIRY_INPUT)
        )
        self.driver.find_element(*self.DELEVIRY_INPUT).click()
        self.driver.find_element(*self.DATE2).click()
        self.driver.find_element(*self.RENTAL_PERIOD).click()
        self.driver.find_element(*self.SECOND_PERIOD).click()
        self.driver.find_element(*self.GREY).click()
        self.driver.find_element(*self.FOR_ORDER_BUTTON).click()
        webdriver.wait(self.driver,5).until(
            EC.visibility_of_element_located(self.FORM_ACCEPT_ORDER)
        )


