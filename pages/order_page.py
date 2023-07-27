import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.order_page_locators import OrderPageForm1Locators, OrderPageForm2Locators, OrderButtonLocators, drop_menu_period, click_date, colour
from links import main_page_scooter, order_page_scooter


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
#        self.driver.maximize_window()

    @allure.step('Открываем главную страницу Самокат')
    def open_page(self):
        self.driver.get(main_page_scooter)

    @allure.step('Открываем форму Заказа')
    def open_order(self):
        self.driver.get(order_page_scooter)

    @allure.step('Ожидание загрузки')
    def waiting(self, locator):
        WebDriverWait(self.driver, 25).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликаем на {button_order} кнопку заказа')
    def click_order_button(self, button_order):
        if button_order == 'top_button':
            self.driver.find_element(*OrderButtonLocators.TOP_BUTTON_ORDER).click()
        elif button_order == 'down_button':
            down_order_button = self.driver.find_element(*OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.driver.execute_script("arguments[0].scrollIntoView();", down_order_button)
            self.waiting(OrderButtonLocators.DOWN_BUTTON_ORDER)
            self.driver.find_element(*OrderButtonLocators.DOWN_BUTTON_ORDER).click()

    @allure.step('Проверяем заголовок 1-й формы заказа')
    def check_heading_order_form1(self):
        actually_value = self.driver.find_element(*OrderPageForm1Locators.ORDER_HEADING_TEXT).text
        expected_value = "Для кого самокат"
        assert expected_value in actually_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Проверяем заголовок 2-й формы заказа')
    def check_heading_order_form2(self):
        actually_value = self.driver.find_element(*OrderPageForm2Locators.ORDER_HEADING_TEXT).text
        expected_value = "Про аренду"
        assert expected_value in actually_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Заполняем поле "Имя"')
    def input_name_form_order(self, name):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_NAME).send_keys(name)

    @allure.step('Заполняем поле "Фамилия"')
    def input_surname_form_order(self, surname):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_SURNAME).send_keys(surname)

    @allure.step('Заполняем поле "Адрес"')
    def input_address_form_order(self, address):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_ADDRESS).send_keys(address)

    @allure.step('Заполняем поле "Станция метро"')
    def input_metro_form_order(self, metro):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_METRO).click()
        self.waiting(OrderPageForm1Locators.METRO_DOWN_LIST)
        self.driver.find_element(*OrderPageForm1Locators.FIELD_INPUT_METRO).send_keys(metro)
        self.driver.find_element(*OrderPageForm1Locators.METRO_DOWN_LIST).click()

    @allure.step('Заполняем поле "Телефон"')
    def input_phone_form_order(self, phone):
        self.driver.find_element(*OrderPageForm1Locators.FIELD_PHONE).send_keys(phone)

    @allure.step('Кликаем по кнопке "Далее"')
    def click_button_next(self):
        self.driver.find_element(*OrderPageForm1Locators.BUTTON_NEXT).click()

    @allure.step('Проверяем заголовок 2-й формы')
    def check_heading_after_click_next_button(self):
        actually_value = self.driver.find_element(*OrderPageForm2Locators.ORDER_HEADING_PAGE2_TEXT).text
        expected_value = "Про аренду"
        assert actually_value == expected_value, f'Ожидалось значение поля Пароль: "{expected_value}", получено "{actually_value}"'

    @allure.step('Заполняем форму "Даты"')
    def input_date_form_order(self, date):
        self.driver.find_element(*OrderPageForm2Locators.FIELD_INPUT_DATE).send_keys(date)
        self.driver.find_element(*click_date(date)).click()

    @allure.step('Заполняем форму "Срок аренды"')
    def input_period_form_order(self, time_period):
        self.driver.find_element(*OrderPageForm2Locators.FIELD_INPUT_PERIOD).click()
        self.waiting(drop_menu_period(time_period))
        self.driver.find_element(*drop_menu_period(time_period)).click()

    @allure.step('Ставим галочку на чекбокс цвета')
    def click_color_checkbox(self, colour_scooter):
        self.driver.find_element(*colour(colour_scooter)).click()

    @allure.step('Заполняем форму "Коментарий курьеру"')
    def input_comment_courier(self, comment):
        self.driver.find_element(*OrderPageForm2Locators.COMMENT_INPUT).send_keys(comment)

    @allure.step('Кликаем по кнопке "Заказать"')
    def click_button_order(self):
        self.driver.find_element(*OrderPageForm2Locators.ORDER_BUTTON).click()

    @allure.step('Кликаем по кнопке "Да"')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageForm2Locators.ORDER_BUTTON_YES).click()

    @allure.step('Проверяем заголовок окна успешного заказа"')
    def check_windows_order_pass(self):
        actually_value = self.driver.find_element(*OrderPageForm2Locators.FINAL_ORDER_WINDOW).text
        expected_value = "Заказ оформлен"
        assert expected_value in actually_value, f'Ожидалось значение поля: "{expected_value}", получено "{actually_value}"'






