from selenium.webdriver.common.by import By
# Главная страница
HOME_PAGE = (By.CLASS_NAME, 'Home_Header__iJKdX')

# Заказ самоката
FORM_ACCEPT_ORDER = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
ACCEPT_BUTTON = (By.XPATH, "//button[text()='Да']")
DELEVIRY_INPUT = (By.XPATH, "//input[@placeholder= '* Когда привезти самокат']")
ORDER_HAS_BEEN = (By.CLASS_NAME ,"Order_Text__2broi")

# Кнопки на странице
SAMOKAT_BUTTON = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
YANDEX_BUTTON = (By.CLASS_NAME , 'Header_Logo__23yGT')