import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.base_page import BasePage
from locators.order_buttons_locator import OrderButton
from locators.locator_page import COOKIE
from locators.for_who_samokat_locators import ForWhoSamokatLocator

class Order_button(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Принять баннер с куки")
    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(COOKIE)
            ).click()
        except:
            pass

    @allure.step("Нажать первую кнопку 'Заказать' на главной странице")
    def first_order_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderButton.ORDER_BUTTON)
        )
        button.click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.NAME)
        )

    @allure.step("Нажать вторую кнопку 'Заказать' внизу страницы")
    def second_order_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(ForWhoSamokatLocator.NAME)
        )
        button.click()