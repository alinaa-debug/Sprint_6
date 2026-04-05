import allure
from page_objects.home_page_object import HomePage
@allure.feature("Главная страница")
class Test_home_page:
   
    @allure.story("Вопрос 1")
    @allure.title("Проверка ответа на первый вопрос.")
    def test_question1(self,driver):
        page = HomePage(driver)
        text = page.question1()
        assert "Сутки — 400 рублей." in text 
    
    @allure.story("Вопрос 2")
    @allure.title("Проверка ответа на второй вопрос")
    def test_question2(self,driver): 
        page = HomePage(driver)
        text = page.question2()
        assert 'Пока что у нас так: один заказ' in text 

    @allure.story("Вопрос 3")
    @allure.title("Проверка ответа на третий вопрос")
    def test_question3(self,driver): 
        page = HomePage(driver)
        text = page.question3()
        assert 'Допустим, вы оформляете заказ на 8 мая' in text
    
    @allure.story("Вопрос 4")
    @allure.title("Проверка ответа на четвертый вопрос")
    def test_question4(self,driver): 
        page = HomePage(driver)
        text = page.question4()
        assert 'Только начиная с завтрашнего дня.' in text

    @allure.story("Вопрос 5")
    @allure.title("Проверка ответа на пятый вопрос")   
    def test_question5(self,driver): 
        page = HomePage(driver)
        text = page.question5()
        assert 'Пока что нет!' in text
    
    @allure.story("Вопрос 6")
    @allure.title("Проверка ответа на шестой вопрос")
    def test_question6(self,driver): 
        page = HomePage(driver)
        text = page.question6()
        assert 'Самокат приезжает к вам с полной зарядкой' in text
    
    @allure.story("Вопрос 7")
    @allure.title("Проверка ответа на седьмой вопрос")
    def test_question7(self,driver): 
        page = HomePage(driver)
        text = page.question7()
        assert 'Да, пока самокат не привезли.' in text 
    
    @allure.story("Вопрос 8")
    @allure.title("Проверка ответа на восьмой вопрос")
    def test_question8(self,driver): 
        page = HomePage(driver)
        text = page.question8()
        assert 'Да, обязательно' in text 

    