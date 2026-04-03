
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.for_who_samokat_locators import ForWhoSamokatLocator


class ForWhoSamokatPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def set_name(self, name):
        self.driver.find_element(*ForWhoSamokatLocator.NAME).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*ForWhoSamokatLocator.SURNAME).send_keys(surname)

    def set_adress(self, adress):
        self.driver.find_element(*ForWhoSamokatLocator.ADRESS).send_keys(adress)

    def set_subway_stations(self):
        self.driver.find_element(*ForWhoSamokatLocator.SUBWAY_STATIONS_DROP_DOWN).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.SUBWAY_STATIONS)
        )
        self.driver.find_element(*ForWhoSamokatLocator.SUBWAY_STATIONS).click()

    def set_phone(self, phone):
        self.driver.find_element(*ForWhoSamokatLocator.PHONE).send_keys(phone)
    def click_further_button(self):
        self.driver.find_element(*ForWhoSamokatLocator.FURTHER_BUTTON).click()


    def filling_data1(self):
        self.set_name("Иван")
        self.set_surname("Иванов")
        self.set_adress("Коммунистический проспект, 35/3")
        self.set_subway_stations()
        self.set_phone("79196917519")
        self.click_further_button()

    
    def filling_data2(self):
        self.set_name("Петр")
        self.set_surname("Петров")
        self.set_adress("Ленинский проспект, 10")
        self.set_subway_stations()
        self.set_phone("79991234567")
        self.click_further_button()