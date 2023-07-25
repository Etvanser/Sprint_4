import allure
from selenium import webdriver
from locators.list_questions import LocatorsList
from pages.list_page import PageList


class TestClickQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @allure.title("Скролим до блока с 'Вопросы о важном' и проверяем его загловок")
    @allure.description("Скролим до блока с 'Вопросы о важном' и проверяем его загловок")
    def test_scroll_list_questions(self):
        list_questions = PageList(self.driver)
        list_questions.open_page()
        list_questions.scroll_to_question_heading()
        list_questions.waiting(LocatorsList.QUESTIONS_HEADING_TEXT)
        list_questions.check_text_question_heading()

    @allure.title('Проверяем 1-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 1-го вопрос блока')
    def test_click_question_1(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_1()
        list_questions.waiting(LocatorsList.QUESTION_1_DROP)
        list_questions.check_text_question_1()

    @allure.title('Проверяем 2-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 2-го вопрос блока')
    def test_click_question_2(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_2()
        list_questions.waiting(LocatorsList.QUESTION_2_DROP)
        list_questions.check_text_question_2()

    @allure.title('Проверяем 3-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 3-го вопрос блока')
    def test_click_question_3(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_3()
        list_questions.waiting(LocatorsList.QUESTION_3_DROP)
        list_questions.check_text_question_3()

    @allure.title('Проверяем 4-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 4-го вопрос блока')
    def test_click_question_4(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_4()
        list_questions.waiting(LocatorsList.QUESTION_4_DROP)
        list_questions.check_text_question_4()

    @allure.title('Проверяем 5-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 5-го вопрос блока')
    def test_click_question_5(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_5()
        list_questions.waiting(LocatorsList.QUESTION_5_DROP)
        list_questions.check_text_question_5()

    @allure.title('Проверяем 6-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 6-го вопрос блока')
    def test_click_question_6(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_6()
        list_questions.waiting(LocatorsList.QUESTION_6_DROP)
        list_questions.check_text_question_6()

    @allure.title('Проверяем 7-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 7-го вопрос блока')
    def test_click_question_7(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_7()
        list_questions.waiting(LocatorsList.QUESTION_7_DROP)
        list_questions.check_text_question_7()

    @allure.title('Проверяем 8-й вопрос блока')
    @allure.description('Проверяем выпадающий текст 8-го вопрос блока')
    def test_click_question_8(self):
        list_questions = PageList(self.driver)
        list_questions.scroll_to_question_heading()
        list_questions.click_question_8()
        list_questions.waiting(LocatorsList.QUESTION_8_DROP)
        list_questions.check_text_question_8()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()



