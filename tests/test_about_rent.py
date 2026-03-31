import allure
from locators import FORM_ACCEPT_ORDER
from page_objects.about_rent_object import SamokatPage


@allure.feature("Заказ самоката")  # Основная функция теста
class TestSamokatOrder:

    @allure.story("Аренда на два дня.")
    @allure.title("Тест: заказ самоката на два дня с черным цветом.")
    def test_rent_first(self,driver):
        page = SamokatPage(driver)
        page.about_rent_first()
        assert driver.find_element(*FORM_ACCEPT_ORDER).is_displayed()
       


    @allure.story("Аренда на один день")
    @allure.title("Тест: заказ самоката на один день с серым цветом")
    def test_rent_second(self,driver):
        page = SamokatPage(driver)
        page.about_rent_second()
        assert driver.find_element(*FORM_ACCEPT_ORDER).is_displayed()

