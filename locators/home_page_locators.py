from selenium.webdriver.common.by import By

class HomePageLocators():


    FIRST_QUESTION = (By.XPATH, "//div[contains(text(), 'Сколько это стоит')]")
    SECOND_QUESTION = (By.XPATH, '//div[text()="Хочу сразу несколько самокатов! Так можно?"]')
    THIRD_QUESTION = (By.XPATH, '//div[text()="Как рассчитывается время аренды?"]')
    FOURTH_QUESTION = (By.XPATH, '//div[text()="Можно ли заказать самокат прямо на сегодня?"]')
    FIFTH_QUESTION = (By.XPATH, '//div[contains(text(), "Можно ли продлить заказ")]')
    SIXTH_QUESTION = (By.XPATH, '//div[contains(text(), "Вы привозите зарядку вместе")]')
    SEVENTH_QUESTION = (By.XPATH, '//div[contains(text(), "Можно ли отменить заказ?")]')
    EIGHTH_QUESTION =(By.XPATH, '//div[contains(text(), "Я жизу за МКАДом, привезёте?")]')

    FIRST_ANSWER = (By.XPATH, '//p[contains(text(), "Сутки — 400 рублей.")]')
    SECOND_ANSWER = (By.XPATH, '//p[contains(text(), "Пока что у нас так:")]')
    THIRD_ANSWER = (By.XPATH, '//p[contains(text(), "Допустим, вы оформляете заказ")]')
    FOURTH_ANSWER = (By.XPATH, '//p[contains(text(), "Только начиная с завтрашнего")]')
    FIFTH_ANSWER = (By.XPATH, '//p[contains(text(), "Пока что нет! Но если")]')
    SIXTH_ANSWER = (By.XPATH, '//p[contains(text(), "Самокат приезжает к вам")]')
    SEVENTH_ANSWER = (By.XPATH, '//p[contains(text(), "Да, пока самокат не привезли.")]')
    EIGHTH_ANSWER = (By.XPATH, '//p[contains(text(), "Да, обязательно")]')