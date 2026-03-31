from selenium.webdriver.common.by import By

class home_page:
    def __init__(self,driver):
        self.driver = driver 
    
    FIRST_QUESTION = (By.XPATH, "//div[@id='accordion__heading-16']")
    SECOND_QUESTION = (By.XPATH, "//div[@id='accordion__heading-17']")
    THIRD_QUESTION = (By.XPATH, "//div[@id='accordion__heading-18']")
    FOURTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-19']")
    FIFTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-20']")
    SIXTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-21']")
    SEVENTH_QUESTION = (By.XPATH, "//div[@id='accordion__heading-22']")
    EIGHTH_QUESTION =(By.XPATH, "//div[@id='accordion__heading-23']")

    FIRST_ANSWER = (By.ID, 'accordion__panel-24')
    SECOND_ANSWER = (By.ID, 'accordion__panel-25')
    THIRD_ANSWER = (By.ID, 'accordion__panel-26')
    FOURTH_ANSWER = (By.ID, 'accordion__panel-27')
    FIFTH_ANSWER = (By.ID, 'accordion__panel-28')
    SIXTH_ANSWER = (By.ID, 'accordion__panel-29')
    SEVENTH_ANSWER = (By.ID, 'accordion__panel-30')
    EIGHTH_ANSWER = (By.ID, 'accordion__panel-31')
    
    def question1(self):
        self.driver.find_element(*self.FIRST_QUESTION).click()
        return self.driver.find_element(*self.FIRST_ANSWER).text
    
    def question2(self):
        self.driver.find_element(*self.SECOND_QUESTION).click()
        return self.driver.find_element(*self.SECOND_ANSWER).text
    
    def question3(self):
        self.driver.find_element(*self.THIRD_QUESTION).click()
        return self.driver.find_element(*self.THIRD_ANSWER).text
    
    def question4(self):
        self.driver.find_element(*self.FOURTH_QUESTION).click()
        return self.driver.find_element(*self.FOURTH_ANSWER).text
    
    def question5(self):
        self.driver.find_element(*self.FIFTH_QUESTION).click()
        return self.driver.find_element(*self.FIFTH_ANSWER).text
    
    def question6(self):
        self.driver.find_element(*self.SIXTH_QUESTION).click()
        return self.driver.find_element(*self.SIXTH_ANSWER).text
    
    def question7(self):
        self.driver.find_element(*self.SEVENTH_QUESTION).click()
        return self.driver.find_element(*self.SEVENTH_ANSWER).text

    def question8(self):
        self.driver.find_element(*self.EIGHTH_QUESTION).click()
        return self.driver.find_element(*self.EIGHTH_ANSWER).text