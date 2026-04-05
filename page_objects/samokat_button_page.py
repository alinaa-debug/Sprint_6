from locators.samocat_button_locators import OrderButtonsLocators


class samokat_button_page:
    def __init__(self,driver2):
        self.driver = driver2

    def click_samocat_button(self):
        self.driver.find_element(*OrderButtonsLocators.SAMOKAT_BUTTON).click()
        

    def click_yandex_button_page(self):
        self.driver.find_element(*OrderButtonsLocators.YANDEX_BUTTON).click()

