import pytest
from selenium import webdriver
from pages.order_page import OrderPage

# Фикстура драйвера FireFox
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

# Фикстура заполнения формы №1
@pytest.fixture
def auto_input_form1(driver):
    page = OrderPage(driver)
    page.open_page()
    page.click_order_button('top_button')
    driver.implicitly_wait(3)
    page.input_name_form_order('Сашкин')
    page.input_surname_form_order('Алинкин')
    page.input_address_form_order('Сосновая 11')
    page.input_metro_form_order('Сокольники')
    page.input_phone_form_order('+79174005566')
    page.click_button_next()
    yield page






