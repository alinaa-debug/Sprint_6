import allure
from page_objects.for_who_samokat_obgect import ForWhoSamokatPage
from page_objects.order_button_page import Order_button
from page_objects.accept_order import AcceptPage
from page_objects.about_rent_object import SamokatPage


@allure.feature("Создание заказа")
@allure.story("Оформление заказа через вторую кнопку")
@allure.title("Создание заказа самоката через вторую кнопку 'Заказать'")
def test_creating_second_order(driver):

    order_page = Order_button(driver)
    for_who_page = ForWhoSamokatPage(driver)
    samokat_page = SamokatPage(driver)
    accept_page = AcceptPage(driver)
    with allure.step("Нажать вторую кнопку 'Заказать'"):
        order_page.second_order_button()

    with allure.step("Заполнить данные пользователя"):
        for_who_page.filling_data2()

    with allure.step("Заполнить информацию об аренде"):
        samokat_page.about_rent_second()

    with allure.step("Подтвердить заказ"):
        accept_page.accept_order_page()

    with allure.step("Проверить переход на страницу оформления заказа"):
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"