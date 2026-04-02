from selenium.webdriver.common.by import By

class AboutRentLocators():
    DELEVIRY_INPUT = [By.XPATH, "//input[@placeholder= '* Когда привезти самокат']"]
    DATE1 = [By.XPATH, "//div[text()= '20']"]
    DATE2 = [By.XPATH, "//div[text()= '18']"]
    RENTAL_PERIOD = [By.XPATH, "//div[text()='* Срок аренды']"]
    FIRST_PERIOD = [By.XPATH, "//div[text()= 'двое суток']"]
    SECOND_PERIOD = [By.XPATH, "//div[text()= 'сутки']"]
    BLACK = [By.ID, "black"]
    GREY = [By.ID, "grey"]
    COMMENT = [By.XPATH, "//input[@placeholder= 'Комментарий для курьера']"]
    FOR_ORDER_BUTTON = [By.XPATH, "//button[text()= 'Заказать']"]
    SUCCESSFUL_ORDER = [By.CLASS_NAME, 'Order_Text__2broi']
    FORM_ACCEPT_ORDER = [By.CLASS_NAME, 'Order_ModalHeader__3FDaJ']
