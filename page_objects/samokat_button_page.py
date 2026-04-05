import allure
from locators.samocat_button_locators import OrderButtonsLocators


class SamokatButtonPage:
    def __init__(self, driver2):
        self.driver = driver2
    @allure.step("Нажать на кнопку 'Самокат'")
    def click_samocat_button(self):
        self.driver.find_element(*OrderButtonsLocators.SAMOKAT_BUTTON).click()

    @allure.step("Нажать на кнопку 'Яндекс'")
    def click_yandex_button_page(self):
        self.driver.find_element(*OrderButtonsLocators.YANDEX_BUTTON).click()

