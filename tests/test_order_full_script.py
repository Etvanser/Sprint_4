import pytest
import allure
from pages.order_page import OrderPage
from data import field_input, nabor


class TestOrderFullScript:

    @allure.title('Полная проверка сценария "Заказать"')
    @allure.description('Полная проверка сценария "Заказать"')
    @pytest.mark.parametrize(field_input, nabor)
    def test_input_form1_order(self, driver, button_order, name, surname, address, metro, phone, date, period, colour_scooter, comment):
        page = OrderPage(driver)
        page.open_page()
        driver.implicitly_wait(25)
        page.click_order_button(button_order)
        page.input_name_form_order(name)
        page.input_surname_form_order(surname)
        page.input_address_form_order(address)
        page.input_metro_form_order(metro)
        page.input_phone_form_order(phone)
        page.click_button_next()
        page.input_date_form_order(date)
        page.input_period_form_order(period)
        page.click_color_checkbox(colour_scooter)
        page.input_comment_courier(comment)
        page.click_button_order()
        page.click_yes_button()
        page.check_windows_order_pass()




