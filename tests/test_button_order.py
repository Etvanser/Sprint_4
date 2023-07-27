import pytest
import allure
from pages.order_page import OrderPage


class TestButtonOrder:

    @allure.title('Проверка кнопок заказа на главной странице')
    @allure.description('Проверяем кнопки "Заказать", верхнию и нижнию')
    @pytest.mark.parametrize('button_order', ['top_button', 'down_button'])
    def test_click_button_order(self, driver, button_order):
        main_page = OrderPage(driver)
        main_page.open_page()
        main_page.driver.implicitly_wait(25)
        main_page.click_order_button(button_order)
        main_page.check_heading_order_form1()

