from selenium.webdriver.common.by import By


class OrderButtonLocators:
    # Верхняя кнопка "Заказать" на главной странице
    TOP_BUTTON_ORDER = By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[contains(text(),'Заказать')]"
    # Нижняя кнопка "Заказать" на главной странице
    DOWN_BUTTON_ORDER = By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[contains(text(),'Заказать')]"


class OrderPageForm1Locators:
    ORDER_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Для кого самокат')]"  # Заголовок формы №1
    FIELD_INPUT_NAME = By.CSS_SELECTOR, 'input[placeholder="* Имя"]'  # Поле ввода имени
    FIELD_INPUT_SURNAME = By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]'  # Поле ввода Фамилии
    FIELD_INPUT_ADDRESS = By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]'  # Поле ввода Адреса
    FIELD_INPUT_METRO = By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]'  # Поле выбора станции метро
    METRO_DOWN_LIST = By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li"  # Выподающий список станций метро
    FIELD_PHONE = By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]'  # Поле ввода телефона
    BUTTON_NEXT = By.XPATH, ".//div/button[contains(text(),'Далее')]"  # Кнопка Далее


class OrderPageForm2Locators:

    ORDER_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Про аренду')]"  # Заголовок формы №2
    FIELD_INPUT_DATE = By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]'  # Поле выбора даты
    FIELD_INPUT_PERIOD = By.XPATH, ".//div[@class='Dropdown-placeholder' and contains(text(),'* Срок аренды')]"  # Поле выбора переода аренды
    COMMENT_INPUT = By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]'  # Поле коментария курьеру
    ORDER_BUTTON = By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and contains(text(),'Заказать')]"  # Кнопка Заказать
    ORDER_BUTTON_YES = By.XPATH, ".//button[contains(text(),'Да')]"  # Кнопка ДА
    FINAL_ORDER_WINDOW = By.XPATH, ".//div[contains(text(),'Заказ оформлен')]"  # Заголовок Финального окна о завершении заказа


# Функция выбора переода аренды
def drop_menu_period(time_period):
    return By.XPATH, f".//div[@role='option' and contains(text(), '{time_period}')]"


# Функция выбора даты
def click_date(date):
    date = date.split('.')[0]
    return By.XPATH, f".//div[contains(@aria-label, '{date}-е')]"


# Функция выбора цвета
def colour(colour_scooter):
    if colour_scooter == 'чёрный жемчуг':
        return By.ID, 'black'
    elif colour_scooter == 'серая безысходность':
        return By.ID, 'grey'

