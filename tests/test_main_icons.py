import allure
from locators.main_page_locators import IconsLocators
from pages.main_page import MainPage
from links import yandex_dzen, main_page_scooter, order_page_scooter


class TestClickIcons:

    @allure.title('Проверяем переход по иконки Самокат')
    @allure.description('Проверка клика по иконки Самокат')
    def test_click_icon_scooter(self, driver):
        main_page = MainPage(driver)
        main_page.opening_page(order_page_scooter)
        main_page.click_button(IconsLocators.ICON_SCOOTER)
        main_page.wait_for_element_to_load(IconsLocators.TEXT_IN_MAIN_PAGE)
        assert main_page.driver.find_element(*IconsLocators.TEXT_IN_MAIN_PAGE)

    @allure.title('Проверяем переход по иконки Яндекс')
    @allure.description('Проверка клика по иконки Яндекс')
    def test_click_icon_yandex(self, driver):
        main_page = MainPage(driver)
        main_page.opening_page(main_page_scooter)
        main_page.click_button(IconsLocators.ICON_YANDEX)
        main_page.swit_window()
        main_page.wait_load_new_window(yandex_dzen)
        main_page.tab_to_open_windows(2)
        assert yandex_dzen in driver.current_url


