import allure
from locators.order_page_locators import OrderPageForm1Locators, OrderPageForm2Locators, OrderButtonLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):

    @allure.step('Кликаем на {button_order} кнопку заказа')
    def click_order_button(self, button_order):
        if button_order == 'top_button':
            self.driver.find_element(*OrderButtonLocators.TOP_BUTTON_ORDER).click()
        elif button_order == 'down_button':
            down_order_button = self.driver.find_element(*OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.driver.execute_script("arguments[0].scrollIntoView();", down_order_button)
            self.wait_for_element_to_load(OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.driver.find_element(*OrderButtonLocators.DOWN_BUTTON_ORDER).click()

    @allure.step('Проверяем заголовок 1-й формы заказа')
    def check_heading_order_form1(self):
        actually_value = self.driver.find_element(*OrderPageForm1Locators.ORDER_HEADING_TEXT).text
        expected_value = "Для кого самокат"
        assert expected_value in actually_value

    @allure.step('Заполняем поле "Станция метро"')
    def input_metro_form_order(self, metro):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_METRO).click()
        self.wait_for_element_to_load(OrderPageForm1Locators.METRO_DOWN_LIST)
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_METRO).send_keys(metro)
        self.driver.find_element(*OrderPageForm1Locators.METRO_DOWN_LIST).click()

    @allure.step('Заполняем форму "Даты"')
    def input_date_form_order(self, date):
        self.driver.find_element(*OrderPageForm2Locators.FIELD_INPUT_DATE).send_keys(date)
        self.driver.find_element(*self.click_date(date)).click()

    @allure.step('Заполняем форму "Срок аренды"')
    def input_period_form_order(self, time_period):
        self.driver.find_element(*OrderPageForm2Locators.FIELD_INPUT_PERIOD).click()
        self.wait_for_element_to_load(self.drop_menu_period(time_period))
        self.driver.find_element(*self.drop_menu_period(time_period)).click()

    @allure.step('Ставим галочку на чекбокс цвета')
    def click_color_checkbox(self, colour_scooter):
        self.driver.find_element(*self.colour(colour_scooter)).click()

    @allure.step('Проверяем заголовок окна успешного заказа"')
    def check_windows_order_pass(self):
        actually_value = self.driver.find_element(*OrderPageForm2Locators.FINAL_ORDER_WINDOW).text
        expected_value = "Заказ оформлен"
        assert expected_value in actually_value

    def drop_menu_period(self, time_period):
        return By.XPATH, f".//div[@role='option' and contains(text(), '{time_period}')]"

    def click_date(self, date):
        date = date.split('.')[0]
        return By.XPATH, f".//div[contains(@aria-label, '{date}-е')]"
    def colour(self, colour_scooter):
        if colour_scooter == 'чёрный жемчуг':
            return OrderPageForm2Locators.COLOUR_BLACK
        elif colour_scooter == 'серая безысходность':
            return OrderPageForm2Locators.COLOUR_GREY






