import allure
from page_objects.accept_order import accept_page
from locators import ORDER_HAS_BEEN

class TestAccept:
    @allure.story("Подтверждение заказа")
    @allure.title("Тест: принять заказ")
    def test_accept_page(self,driver):
        page = accept_page(driver)
        page.accept_order_page()
        assert page.driver.find_element(*ORDER_HAS_BEEN).is_displayed()


