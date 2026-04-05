from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def question1(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FIRST_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FIRST_ANSWER).text

    def question2(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SECOND_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SECOND_ANSWER).text
    
    def question3(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.THIRD_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.THIRD_ANSWER).text
    
    def question4(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FOURTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FOURTH_ANSWER).text
    
    def question5(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FIFTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FIFTH_ANSWER).text
    
    def question6(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SIXTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SIXTH_ANSWER).text
    
    def question7(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SEVENTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SEVENTH_ANSWER).text

    def question8(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.EIGHTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.EIGHTH_ANSWER).text