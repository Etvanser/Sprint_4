import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу {link}')
    def opening_page(self, link):
        self.driver.get(link)

    @allure.step('Переключаемся на открывшаеся окно')
    def swit_window(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])

    @allure.step('Кликаем по {locator}')
    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Заполняем поле {locator}')
    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Ожидание загрузки {locator}')
    def wait_for_element_to_load(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))

    def wait_load_new_window(self, link):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(link))

    def tab_to_open_windows(self, tab):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(tab))
