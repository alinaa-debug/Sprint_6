import allure
from page_objects.order_button_page import Order_button

@allure.feature("Кнопки заказа")
class Test_samokat_button:
    
    @allure.story("Верхняя кнопка заказа")
    @allure.title("Проверка верхней кнопки 'Заказать'")
    def test_first_order_button(self,driver):
        page = Order_button(driver)
        page.first_order_button()
        assert driver.find_element(*page.NAME).is_displayed()

    @allure.story("Нижняя кнопка заказа")
    @allure.title("Проверка нижней кнопки 'Заказать'")
    def test_second_order_button(self,driver):
        page = Order_button(driver)
        page.second_order_button()
        assert driver.find_element(*page.NAME).is_displayed()
          