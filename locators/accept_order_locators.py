from selenium.webdriver.common.by import By
    
class AcceptOrderLocators():
    FORM_ACCEPT_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    ACCEPT_BUTTON = (By.XPATH, "//button[text()='Да']")
    ORDER_HAS_BEEN = (By.CLASS_NAME ,"Order_Text__2broi")
