import allure
from locators.main_page_locators import LocatorsList
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_question(self):
        return self.driver.find_elements(*LocatorsList.LOCATOR_QUESTIONS)

    @allure.step('Кликаем на вопрос {iq_q}')
    def click_question(self, iq_q):
        question = self.get_question()
        question[iq_q - 1].click()

    @allure.step('Получаем ответ на вопрос')
    def get_question_text(self):
        return self.driver.find_element(*LocatorsList.LOCATOR_FAQ_ANSWER).text

    @allure.step('Скролим страницу до Важных ответов')
    def scroll_to_question_heading(self):
        text_question_heading = self.driver.find_element(*LocatorsList.QUESTIONS_HEADING_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", text_question_heading)




