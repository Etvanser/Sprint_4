from selenium.webdriver.common.by import By


class LocatorsList:

    QUESTIONS_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Вопросы о важном')]"
    LOCATOR_FAQ_ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")
    LOCATOR_QUESTIONS = By.XPATH, "//div[contains(@class, 'accordion__item')]"


class IconsLocators:

    ICON_YANDEX = By.XPATH, '//img[@alt="Yandex"]'  # Иконка Яндекс
    ICON_SCOOTER = By.XPATH, '//img[@alt="Scooter"]'  # Иконка Самокат
    TEXT_IN_MAIN_PAGE = By.XPATH, ".//div[contains(text(),'Привезём его прямо к вашей двери,')]"

