from selenium.webdriver.common.by import By


class TextQuestion:

    text_question1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    text_question2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто' \
                     ' сделать несколько заказов — один за другим.'
    text_question3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени' \
                     ' аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в' \
                     ' 20:30, суточная аренда закончится 9 мая в 20:30.'
    text_question4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    text_question5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру' \
                     ' 1010.'
    text_question6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете' \
                     ' кататься без передышек и во сне. Зарядка не понадобится.'
    text_question7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим.' \
                     ' Все же свои.'
    text_question8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'


class LocatorsList:

    QUESTIONS_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Вопросы о важном')]"
    QUESTION_1 = By.XPATH, ".//div[contains(text(),'Сколько это стоит? И как оплатить?')]"
    QUESTION_2 = By.XPATH, ".//div[contains(text(),'Хочу сразу несколько самокатов! Так можно?')]"
    QUESTION_3 = By.XPATH, ".//div[contains(text(),'Как рассчитывается время аренды?')]"
    QUESTION_4 = By.XPATH, ".//div[contains(text(),'Можно ли заказать самокат прямо на сегодня?')]"
    QUESTION_5 = By.XPATH, ".//div[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?')]"
    QUESTION_6 = By.XPATH, ".//div[contains(text(),'Вы привозите зарядку вместе с самокатом?')]"
    QUESTION_7 = By.XPATH, ".//div[contains(text(),'Можно ли отменить заказ?')]"
    QUESTION_8 = By.XPATH, ".//div[contains(text(),'Я жизу за МКАДом, привезёте?')]"

    QUESTION_1_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question1}')]"
    QUESTION_2_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question2}')]"
    QUESTION_3_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question3}')]"
    QUESTION_4_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question4}')]"
    QUESTION_5_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question5}')]"
    QUESTION_6_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question6}')]"
    QUESTION_7_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question7}')]"
    QUESTION_8_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question8}')]"

    QUESTION_1_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-0' and not(@hidden)]"
    QUESTION_2_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-1' and not(@hidden)]"
    QUESTION_3_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-2' and not(@hidden)]"
    QUESTION_4_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-3' and not(@hidden)]"
    QUESTION_5_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-4' and not(@hidden)]"
    QUESTION_6_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-5' and not(@hidden)]"
    QUESTION_7_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-6' and not(@hidden)]"
    QUESTION_8_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-7' and not(@hidden)]"
#    LOCATOR_FAQ_ANSWER = (By.XPATH, "//div[contains(@class, 'accordion__panel') and not(@hidden)]")


