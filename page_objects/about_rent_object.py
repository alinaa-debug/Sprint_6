
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.about_rent_locators import AboutRentLocators

class SamokatPage(BasePage):

    @allure.step("Выбор даты аренды и срок аренды")
    def select_date_and_period(self, date_locator, period_locator):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(AboutRentLocators.DELEVIRY_INPUT)
        ).click()
        self.driver.find_element(*date_locator).click()
        self.driver.find_element(*AboutRentLocators.RENTAL_PERIOD).click()
        self.driver.find_element(*period_locator).click()

    @allure.step("Выбор цвета самоката")
    def select_color(self, color_locator):
        self.driver.find_element(*color_locator).click()

    @allure.step("Ввод комментария для курьера")
    def enter_comment(self, comment):
        self.driver.find_element(*AboutRentLocators.COMMENT).send_keys(comment)

    @allure.step("Нажатие кнопки 'Заказать'")
    def click_order_button(self):
        self.driver.find_element(*AboutRentLocators.FOR_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(AboutRentLocators.FORM_ACCEPT_ORDER)
        )

    @allure.step("Заполнить форму аренды - первый вариант")
    def fill_rent_first(self, user_data):
        self.select_date_and_period(AboutRentLocators.DATE1, AboutRentLocators.FIRST_PERIOD)
        self.select_color(AboutRentLocators.BLACK)
        self.enter_comment(user_data['comment'])
        self.click_order_button()

    @allure.step("Заполнить форму аренды - второй вариант")
    def fill_rent_second(self, user_data):
        self.select_date_and_period(AboutRentLocators.DATE2, AboutRentLocators.SECOND_PERIOD)
        self.select_color(AboutRentLocators.GREY)
        self.enter_comment(user_data['comment'])
        self.click_order_button()