import allure
from locators.main_page_locators import LocatorsList
from pages.main_page import MainPage


class TestClickQuestions:

    @allure.title("Скролим до блока с 'ответы о важном' и проверяем его загловок")
    @allure.description("Скролим до блока с 'ответы о важном' и проверяем его загловок")
    def test_scroll_list_questions(self, driver):
        list_questions = MainPage(driver)
        list_questions.open_page()
        list_questions.scroll_to_question_heading()
        list_questions.waiting(LocatorsList.QUESTIONS_HEADING_TEXT)
        list_questions.check_text_question_heading()

    @allure.title('Проверяем 1-й ответ блока')
    @allure.description('Проверяем выпадающий текст 1-го ответ блока')
    def test_click_question_1(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_1()
        list_questions.waiting(LocatorsList.QUESTION_1_DROP)
        list_questions.check_text_question_1()

    @allure.title('Проверяем 2-й ответ блока')
    @allure.description('Проверяем выпадающий текст 2-го ответ блока')
    def test_click_question_2(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_2()
        list_questions.waiting(LocatorsList.QUESTION_2_DROP)
        list_questions.check_text_question_2()

    @allure.title('Проверяем 3-й ответ блока')
    @allure.description('Проверяем выпадающий текст 3-го ответ блока')
    def test_click_question_3(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_3()
        list_questions.waiting(LocatorsList.QUESTION_3_DROP)
        list_questions.check_text_question_3()

    @allure.title('Проверяем 4-й ответ блока')
    @allure.description('Проверяем выпадающий текст 4-го ответ блока')
    def test_click_question_4(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_4()
        list_questions.waiting(LocatorsList.QUESTION_4_DROP)
        list_questions.check_text_question_4()

    @allure.title('Проверяем 5-й ответ блока')
    @allure.description('Проверяем выпадающий текст 5-го ответ блока')
    def test_click_question_5(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_5()
        list_questions.waiting(LocatorsList.QUESTION_5_DROP)
        list_questions.check_text_question_5()

    @allure.title('Проверяем 6-й ответ блока')
    @allure.description('Проверяем выпадающий текст 6-го ответ блока')
    def test_click_question_6(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_6()
        list_questions.waiting(LocatorsList.QUESTION_6_DROP)
        list_questions.check_text_question_6()

    @allure.title('Проверяем 7-й ответ блока')
    @allure.description('Проверяем выпадающий текст 7-го ответ блока')
    def test_click_question_7(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_7()
        list_questions.waiting(LocatorsList.QUESTION_7_DROP)
        list_questions.check_text_question_7()

    @allure.title('Проверяем 8-й ответ блока')
    @allure.description('Проверяем выпадающий текст 8-го ответ блока')
    def test_click_question_8(self, driver):
        list_questions = MainPage(driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_8()
        list_questions.waiting(LocatorsList.QUESTION_8_DROP)
        list_questions.check_text_question_8()
