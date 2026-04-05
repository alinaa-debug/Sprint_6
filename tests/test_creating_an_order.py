import allure
from page_objects.for_who_samokat_obgect import ForWhoSamokatPage
from page_objects.order_button_page import Order_button
from page_objects.about_rent_object import SamokatPage
from page_objects.accept_order import AcceptPage
from data import Users  

@allure.feature("Создание заказа")
class TestOrderPage:

    @allure.title("тест на оформление заказа через кнопку заказа в хедере")
    @allure.description(
        "1. Принять куки\n"
        "2. Кликнуть кнопку 'Заказать' в хедере\n"
        "3. Заполнить форму о себе и нажать далее\n"
        "4. Заполнить форму о заказе и нажать 'Заказать'"
    )
    def test_order_by_header_order_button_true(self, driver):
        
        # Создаём объекты страниц
        order_page = Order_button(driver)
        for_who_page = ForWhoSamokatPage(driver)
        samokat_page = SamokatPage(driver)
        accept_page = AcceptPage(driver)


        # 1. Принять куки
        order_page.accept_cookies()

        # 2. Кликнуть первую кнопку "Заказать"
        order_page.first_order_button()

        # 3. Заполнить форму о себе
        for_who_page.complete_send_field_about_person(Users.user_1)

        # 4. Заполнить форму о заказе
        samokat_page.fill_rent_first(Users.user_1)

        # 5. Подтвердить заказ
        accept_page.accept_order_page()

        # Проверка URL
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"