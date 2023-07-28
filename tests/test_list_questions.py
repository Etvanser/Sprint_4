import allure
import pytest
from locators.main_page_locators import LocatorsList
from pages.main_page import MainPage
from links import main_page_scooter
from data import QuestionsData


class TestClickQuestions:

    @allure.title("Скролим до блока с 'Вопросы о важном' и проверяем каждый вопрос")
    @allure.description("Открываем вопрос {id_q} и проверяем ответ {text_q}")
    @pytest.mark.parametrize(QuestionsData.param, QuestionsData.param_value)
    def test_scroll_list_questions(self, driver, id_q, text_q):
        main_page = MainPage(driver)
        main_page.opening_page(main_page_scooter)
        main_page.scroll_to_question_heading()
        main_page.wait_for_element_to_load(LocatorsList.QUESTIONS_HEADING_TEXT)
        main_page.click_question(id_q)
        main_page.wait_for_element_to_load(LocatorsList.LOCATOR_FAQ_ANSWER)
        text_question = main_page.get_question_text()
        assert text_question == text_q

