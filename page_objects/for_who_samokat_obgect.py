
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.for_who_samokat_locators import ForWhoSamokatLocator
import allure

class ForWhoSamokatPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнение поля 'Имя'")
    def send_name_to_name_field(self, text):
        self.send_keys(ForWhoSamokatLocator.NAME, text)

    @allure.step("Заполнение поля 'Фамилия'")
    def send_last_name_to_name_field(self, text):
        self.send_keys(ForWhoSamokatLocator.SURNAME, text)

    @allure.step("Заполнение поля 'Адрес'")
    def send_address_to_address_field(self, text):
        self.send_keys(ForWhoSamokatLocator.ADRESS, text)

    @allure.step("Выбор станции метро")
    def send_metro_station_to_metro_station_field(self):
        self.click_button(ForWhoSamokatLocator.SUBWAY_STATIONS_DROP_DOWN)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.SUBWAY_STATIONS)
        )
        self.click_button(ForWhoSamokatLocator.SUBWAY_STATIONS)

    @allure.step("Заполнение поля 'Телефон'")
    def send_telephone_number_to_telephone_number_field(self, text):
        self.send_keys(ForWhoSamokatLocator.PHONE, text)

    @allure.step("Клик на кнопку 'Далее'")
    def click_on_the_next_button(self):
        self.click_button(ForWhoSamokatLocator.FURTHER_BUTTON)


    allure.step("Полное заполнение информации о пользователе")
    def complete_send_field_about_person(self, user):
        
        self.send_name_to_name_field(user['first_name'])
        self.send_last_name_to_name_field(user['last_name'])
        self.send_address_to_address_field(user['address'])
        self.send_metro_station_to_metro_station_field()
        self.send_telephone_number_to_telephone_number_field(user['phone'])
        self.click_on_the_next_button()    