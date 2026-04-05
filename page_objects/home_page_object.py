import allure
from page_objects.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Открыть первый вопрос и получить ответ")
    def question1(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FIRST_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FIRST_ANSWER).text


    @allure.step("Открыть второй вопрос и получить ответ")
    def question2(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SECOND_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SECOND_ANSWER).text

    @allure.step("Открыть третий вопрос и получить ответ")
    def question3(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.THIRD_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.THIRD_ANSWER).text

    @allure.step("Открыть четвертый вопрос и получить ответ")
    def question4(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FOURTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FOURTH_ANSWER).text

    @allure.step("Открыть пятый вопрос и получить ответ")
    def question5(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.FIFTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.FIFTH_ANSWER).text

    @allure.step("Открыть шестой вопрос и получить ответ")
    def question6(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SIXTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SIXTH_ANSWER).text

    @allure.step("Открыть седьмой вопрос и получить ответ")
    def question7(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.SEVENTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.SEVENTH_ANSWER).text

    @allure.step("Открыть восьмой вопрос и получить ответ")
    def question8(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element(*HomePageLocators.EIGHTH_QUESTION).click()
        return self.driver.find_element(*HomePageLocators.EIGHTH_ANSWER).text