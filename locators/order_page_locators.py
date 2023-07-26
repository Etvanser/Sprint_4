from selenium.webdriver.common.by import By


class OrderButtonLocators:

    TOP_BUTTON_ORDER = By.XPATH, ".//div[@class='Header_Nav__AGCXC'/button[contains(text(),'Заказать')]"
    DOWN_BUTTON_ORDER = By.XPATH, ".//div[@class='Home_FinishButton__1_cWm'/button[contains(text(),'Заказать')"


class OrderPageLocators:

    ORDER_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Для кого самокат')]"
