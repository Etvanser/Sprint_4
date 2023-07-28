import pytest
import allure
from pages.order_page import OrderPage
from links import main_page_scooter
from locators.order_page_locators import OrderPageForm1Locators


class TestButtonOrder:

    @allure.title('Проверка кнопок заказа на главной странице')
    @allure.description('Проверяем кнопки "Заказать", верхнию и нижнию')
    @pytest.mark.parametrize('button_order', ['top_button', 'down_button'])
    def test_click_button_order(self, driver, button_order):
        main_page = OrderPage(driver)
        main_page.opening_page(main_page_scooter)
        main_page.click_order_button(button_order)
        main_page.wait_for_element_to_load(OrderPageForm1Locators.ORDER_HEADING_TEXT)
        main_page.check_heading_order_form1()

