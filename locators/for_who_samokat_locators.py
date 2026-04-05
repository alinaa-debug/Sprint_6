from selenium.webdriver.common.by import By

class ForWhoSamokatLocator():


    NAME =(By.XPATH, ".//input[placeholder='* Имя']")
    SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_STATIONS_DROP_DOWN = (By.XPATH, "//div[@class = 'select-search__value']")
    SUBWAY_STATIONS = (By.XPATH, '//input[@value="Черкизовская"]')
    PHONE = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")
    FURTHER_BUTTON = (By.XPATH, "//button[text()= 'Далее']")
    