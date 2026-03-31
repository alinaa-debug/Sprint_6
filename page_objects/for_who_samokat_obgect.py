from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from data import login



class samokat_page:
    NAME =(By.XPATH, "//input[placeholder='* Имя']")
    SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    SUBWAY_STATIONS_DROP_DOWN = (By.XPATH, "//div[@class = 'select-search__value']")
    PHONE = (By.XPATH,"//input[@placeholder='* Телефон: на него позвонит курьер']")
    FURTHER_BUTTON = (By.XPATH, "//button[text()= 'Далее']")
    
    def __init__(self,driver):
        self.driver = driver 
    

    def set_name(self,name):
        webdriver.wait(self.driver,5).until(
        EC.visibility_of_element_located(self.NAME)
        )
        self.driver.find_element(*self.NAME).send_keys(name)

    def set_surname(self,surname):
        self.driver.find_element(*self.SURNAME).send_keys(surname)

    def set_adress(self,adress):    
        self.driver.find_element(*self.ADRESS).send_keys(adress)

    def set_subway_stations(self,station):    
        self.driver.find_element(*self.SUBWAY_STATIONS_DROP_DOWN).send_keys(station)

    def set_phone(self,phone):   
        self.driver.find_element(*self.PHONE).send_keys(phone)

    def click_further_button(self):
        self.driver.find_element(*self.FURTHER_BUTTON).click()


    def filling_data(self,data):
        self.set_name(data["name"])
        self.set_surname(data["surname"])
        self.set_adress(data["adress"])
        self.set_subway_stations(data["station"])
        self.set_phone(data["phone"])
        self.click_further_button()   
        
        
    

