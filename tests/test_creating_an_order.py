import allure
from page_objects.for_who_samokat_obgect import ForWhoSamokatPage
from page_objects.order_button_page import Order_button
from page_objects.accept_order import AcceptPage
from page_objects.about_rent_object import SamokatPage

@allure.feature("Создание заказа")
@allure.story("Пользователь может оформить заказ самоката")
@allure.title("Тест оформления заказа через кнопку 'Заказать'")
def test_creating_an_order(driver):

    order_page = Order_button(driver)
    for_who_page = ForWhoSamokatPage(driver)
    samokat_page = SamokatPage(driver)
    accept_page = AcceptPage(driver)

    with allure.step("Принять cookies"):
        order_page.accept_cookies()

    with allure.step("Нажать кнопку 'Заказать'"):
        order_page.first_order_button()

    with allure.step("Заполнить данные пользователя"):
        for_who_page.filling_data1()

    with allure.step("Заполнить данные аренды"):
        samokat_page.about_rent_first()

    with allure.step("Подтвердить заказ"):
        accept_page.accept_order_page()

    with allure.step("Проверить переход на страницу заказа"):
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"    