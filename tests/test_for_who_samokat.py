import pytest
import allure
from page_objects.for_who_samokat_obgect import samokat_page
from data import order_data
from locators import DELEVIRY_INPUT

@allure.feature("Заказ самоката")
class Test_samokat_obgect:
    
    @allure.story("Форма заказа")
    @pytest.mark.parametrize("data",
                             order_data.orders,
                             ids= ["filling_data: 1", "filling_data: 2"])
    def test_for_who_samocat_object(self,driver,data):
        page = samokat_page(driver)
        page.filling_data(data)
        assert driver.find_element(*DELEVIRY_INPUT).is_displayed()


     









