import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.accept_order_locators import AcceptOrderLocators
from page_objects.base_page import BasePage

class AcceptPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Ожидание появления формы подтверждения заказа")
    def wait_for_accept_form(self):
        WebDriverWait(self.driver, 5).until(
          EC.visibility_of_element_located(AcceptOrderLocators.FORM_ACCEPT_ORDER)

        )


    @allure.step("Подтверждение заказа кнопкой 'Да'")
    def click_accept_button(self):
        self.driver.find_element(*AcceptOrderLocators.ACCEPT_BUTTON).click()


    @allure.step("Проверка успешного оформления заказа")
    def wait_for_order_confirmation(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(AcceptOrderLocators.ORDER_HAS_BEEN)

        )

    @allure.step("Принять заказ полностью")
    def accept_order_page(self):
        self.wait_for_accept_form()
        self.click_accept_button()
        self.wait_for_order_confirmation()