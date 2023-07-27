import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.main_page_locators import IconsLocators
from pages.main_page import MainPage
from links import yandex_dzen


class TestClickIcons:

    @allure.title('Проверяем переход по иконки Самокат')
    @allure.description('Проверка клика по иконки Самокат')
    def test_click_icon_scooter(self, driver, auto_input_form1):
        main_page = auto_input_form1
        main_page.driver.find_element(*IconsLocators.ICON_SCOOTER).click()
        assert driver.find_element(*IconsLocators.MAIN_IMG)

    @allure.title('Проверяем переход по иконки Яндекс')
    @allure.description('Проверка клика по иконки Яндекс')
    def test_click_icon_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.click_yandex_icon()
        main_page.swit_window()
        WebDriverWait(driver, 25).until(expected_conditions.url_to_be(yandex_dzen))
        WebDriverWait(driver, 25).until(expected_conditions.number_of_windows_to_be(2))
        assert yandex_dzen in driver.current_url


