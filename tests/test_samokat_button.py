import allure 
from page_objects.samokat_button_page import samokat_button_page
from locators.locator_page import HOME_PAGE
@allure.feature("Кнопки самоката")
class Test_samokat_button:
    
    @allure.story("Кнопка самокат")
    def test_samocat_button(self,driver):
        page = samokat_button_page(driver)
        page.click_samocat_button()
        correct_input = driver.find_element(*HOME_PAGE)
        assert correct_input.is_displayed()


    @allure.story("Кнопка Яндекс")
    def test_yandex_button(self,driver):
        page = samokat_button_page(driver)
        page.click_yandex_button_page()
        driver.switch_to.window(driver.window_handles[1])
        assert 'dzen.ru' in driver.current_url 