
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.about_rent_locators import AboutRentLocators

class SamokatPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


   
    def about_rent_first(self):
        WebDriverWait(self.driver,5).until(
        EC.visibility_of_element_located(AboutRentLocators.DELEVIRY_INPUT)
        )
        self.driver.find_element(*AboutRentLocators.DELEVIRY_INPUT).click()
        self.driver.find_element(*AboutRentLocators.DATE1).click()
        self.driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*AboutRentLocators.FIRST_PERIOD).click()
        self.driver.find_element(*AboutRentLocators.BLACK).click()
        self.driver.find_element(*AboutRentLocators.COMMENT).click()
        self.driver.find_element(*AboutRentLocators.FOR_ORDER_BUTTON).click()
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(AboutRentLocators.FORM_ACCEPT_ORDER)
        )

    def about_rent_second(self):
        WebDriverWait(self.driver,5).until(
        EC.visibility_of_element_located(AboutRentLocators.DELEVIRY_INPUT)
        )
        self.driver.find_element(*AboutRentLocators.DELEVIRY_INPUT).click()
        self.driver.find_element(*AboutRentLocators.DATE2).click()
        self.driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*AboutRentLocators.SECOND_PERIOD).click()
        self.driver.find_element(*AboutRentLocators.GREY).click()
        self.driver.find_element(*AboutRentLocators.FOR_ORDER_BUTTON).click()
        WebDriverWait(self.driver,5).until(
            EC.visibility_of_element_located(AboutRentLocators.FORM_ACCEPT_ORDER)
        )


