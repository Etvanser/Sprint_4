import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.main_page_locators import LocatorsList, TextQuestion, IconsLocators
from links import yandex_dzen, main_page_scooter, order_page_scooter


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()

    @allure.step('Открываем страницу')
    def open_page(self, ):
        self.driver.get(main_page_scooter)

    @allure.step('Ожидание загрузки')
    def waiting(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем по иконке Яндекс')
    def click_yandex_icon(self):
        self.driver.find_element(*IconsLocators.ICON_YANDEX).click()

    @allure.step('Переключаемся на открывшаеся окно')
    def swit_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    @allure.step('Скролим страницу до Важных ответов')
    def scroll_to_question_heading(self):
        text_question_heading = self.driver.find_element(*LocatorsList.QUESTIONS_HEADING_TEXT)
        self.driver.execute_script("arguments[0].scrollIntoView();", text_question_heading)

    @allure.step('Проверяем текст заголовка с ответами')
    def check_text_question_heading(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTIONS_HEADING_TEXT).text
        expected_value = "Вопросы о важном"
        assert expected_value in actually_value, f'Ожидалось значение поля: "{expected_value}", получено "{actually_value}"'

    @allure.step('Кликаем на 1-й ответ')
    def click_question_1(self):
        self.driver.find_element(*LocatorsList.QUESTION_1).click()

    @allure.step('Кликаем на 2-й ответ')
    def click_question_2(self):
        self.driver.find_element(*LocatorsList.QUESTION_2).click()

    @allure.step('Кликаем на 3-й ответ')
    def click_question_3(self):
        self.driver.find_element(*LocatorsList.QUESTION_3).click()

    @allure.step('Кликаем на 4-й ответ')
    def click_question_4(self):
        self.driver.find_element(*LocatorsList.QUESTION_4).click()

    @allure.step('Кликаем на 5-й ответ')
    def click_question_5(self):
        self.driver.find_element(*LocatorsList.QUESTION_5).click()

    @allure.step('Кликаем на 6-й ответ')
    def click_question_6(self):
        self.driver.find_element(*LocatorsList.QUESTION_6).click()

    @allure.step('Кликаем на 7-й ответ')
    def click_question_7(self):
        self.driver.find_element(*LocatorsList.QUESTION_7).click()

    @allure.step('Кликаем на 8-й ответ')
    def click_question_8(self):
        self.driver.find_element(*LocatorsList.QUESTION_8).click()

    @allure.step('Проверяем текст 1-го ответа')
    def check_text_question_1(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_1_DROP_TEXT).text
        expected_value = TextQuestion.text_question1
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 2-го ответа')
    def check_text_question_2(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_2_DROP_TEXT).text
        expected_value = TextQuestion.text_question2
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 3-го ответа')
    def check_text_question_3(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_3_DROP_TEXT).text
        expected_value = TextQuestion.text_question3
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 4-го ответа')
    def check_text_question_4(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_4_DROP_TEXT).text
        expected_value = TextQuestion.text_question4
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 5-го ответа')
    def check_text_question_5(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_5_DROP_TEXT).text
        expected_value = TextQuestion.text_question5
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 6-го ответа')
    def check_text_question_6(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_6_DROP_TEXT).text
        expected_value = TextQuestion.text_question6
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 7-го ответа')
    def check_text_question_7(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_7_DROP_TEXT).text
        expected_value = TextQuestion.text_question7
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем текст 8-го ответа')
    def check_text_question_8(self):
        actually_value = self.driver.find_element(*LocatorsList.QUESTION_8_DROP_TEXT).text
        expected_value = TextQuestion.text_question8
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'


