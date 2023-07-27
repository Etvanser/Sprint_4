import pytest
import allure
from pages.order_page import OrderPage
from data import field_input_from_1, field_input_from_2, value_input_form_1, value_input_form_2


class TestFormOrder:

    @allure.title('Проверяем заполнение формы заказа №1')
    @allure.description('Проверка заполнение формы №1')
    @pytest.mark.parametrize(field_input_from_1, value_input_form_1)
    def test_form1_order(self, driver, button_order, name, surname, address, metro, phone):
        page = OrderPage(driver)
        page.open_page()
        page.click_order_button(button_order)
        page.driver.implicitly_wait(25)
        page.input_name_form_order(name)
        page.input_surname_form_order(surname)
        page.input_address_form_order(address)
        page.input_metro_form_order(metro)
        page.input_phone_form_order(phone)
        page.click_button_next()
        page.check_heading_order_form2()

    @allure.title('Проверяем заполнение формы заказа №2')
    @allure.description('Проверка заполнение формы №2')
    @pytest.mark.parametrize(field_input_from_2, value_input_form_2)
    def test_form2_order(self, auto_input_form1, date, period, colour_scooter, comment):
        page = auto_input_form1
        page.driver.implicitly_wait(25)
        page.input_date_form_order(date)
        page.input_period_form_order(period)
        page.click_color_checkbox(colour_scooter)
        page.input_comment_courier(comment)
        page.click_button_order()
        page.click_yes_button()
        page.check_windows_order_pass()


