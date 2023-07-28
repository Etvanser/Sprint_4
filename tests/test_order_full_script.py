import pytest
import allure
from pages.order_page import OrderPage
from data import DataTest
from links import main_page_scooter
from locators.order_page_locators import OrderPageForm1Locators, OrderPageForm2Locators


class TestOrderFullScript:

    @allure.title('Полная проверка сценария "Заказать"')
    @allure.description('Полная проверка сценария "Заказать"')
    @pytest.mark.parametrize(DataTest.field_input, DataTest.nabor)
    def test_input_form1_order(self, driver, button_order, name, surname, address, metro, phone, date, period,
                               colour_scooter, comment):
        page = OrderPage(driver)
        page.opening_page(main_page_scooter)
        page.click_order_button(button_order)
        page.wait_for_element_to_load(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        page.input_text(OrderPageForm1Locators.FIELD_INPUT_NAME, name)
        page.input_text(OrderPageForm1Locators.FIELD_INPUT_SURNAME, surname)
        page.input_text(OrderPageForm1Locators.FIELD_INPUT_ADDRESS, address)
        page.input_metro_form_order(metro)
        page.input_text(OrderPageForm1Locators.FIELD_PHONE, phone)
        page.click_button(OrderPageForm1Locators.BUTTON_NEXT)
        page.wait_for_element_to_load(OrderPageForm2Locators.ORDER_HEADING_TEXT)
        page.input_date_form_order(date)
        page.input_period_form_order(period)
        page.click_color_checkbox(colour_scooter)
        page.input_text(OrderPageForm2Locators.COMMENT_INPUT, comment)
        page.click_button(OrderPageForm2Locators.ORDER_BUTTON)
        page.wait_for_element_to_load(OrderPageForm2Locators.ORDER_BUTTON_YES)
        page.click_button(OrderPageForm2Locators.ORDER_BUTTON_YES)
        page.wait_for_element_to_load(OrderPageForm2Locators.FINAL_ORDER_WINDOW)
        page.check_windows_order_pass()




