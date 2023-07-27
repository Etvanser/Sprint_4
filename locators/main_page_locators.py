from selenium.webdriver.common.by import By


class TextQuestion:  # Класс ответов на ответы в списке "Вопросы о важном"

    text_question1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'  # 1-й ответ
    text_question2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто' \
                     ' сделать несколько заказов — один за другим.'  # 2-й ответ
    text_question3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени' \
                     ' аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в' \
                     ' 20:30, суточная аренда закончится 9 мая в 20:30.'  # 3-й ответ
    text_question4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'  # 4-й ответ
    text_question5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру' \
                     ' 1010.'  # 5-й ответ
    text_question6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете' \
                     ' кататься без передышек и во сне. Зарядка не понадобится.'  # 6-й ответ
    text_question7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим.' \
                     ' Все же свои.'  # 7-й ответ
    text_question8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'  # 8-й ответ


class LocatorsList:

    QUESTIONS_HEADING_TEXT = By.XPATH, ".//div[contains(text(),'Вопросы о важном')]"
    QUESTION_1 = By.XPATH, ".//div[contains(text(),'Сколько это стоит? И как оплатить?')]"  # 1-й вопрос
    QUESTION_2 = By.XPATH, ".//div[contains(text(),'Хочу сразу несколько самокатов! Так можно?')]"  # 2-й вопрос
    QUESTION_3 = By.XPATH, ".//div[contains(text(),'Как рассчитывается время аренды?')]"  # 3-й вопрос
    QUESTION_4 = By.XPATH, ".//div[contains(text(),'Можно ли заказать самокат прямо на сегодня?')]"  # 4-й вопрос
    QUESTION_5 = By.XPATH, ".//div[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?')]"  # 5-й вопрос
    QUESTION_6 = By.XPATH, ".//div[contains(text(),'Вы привозите зарядку вместе с самокатом?')]"  # 6-й вопрос
    QUESTION_7 = By.XPATH, ".//div[contains(text(),'Можно ли отменить заказ?')]"  # 7-й вопрос
    QUESTION_8 = By.XPATH, ".//div[contains(text(),'Я жизу за МКАДом, привезёте?')]"  # 8-й вопрос

    QUESTION_1_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question1}')]"  # Выподающий ответ #1
    QUESTION_2_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question2}')]"  # Выподающий ответ #2
    QUESTION_3_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question3}')]"  # Выподающий ответ #3
    QUESTION_4_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question4}')]"  # Выподающий ответ #4
    QUESTION_5_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question5}')]"  # Выподающий ответ #5
    QUESTION_6_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question6}')]"  # Выподающий ответ #6
    QUESTION_7_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question7}')]"  # Выподающий ответ #7
    QUESTION_8_DROP_TEXT = By.XPATH, f".//div/p[contains(text(),'{TextQuestion.text_question8}')]"  # Выподающий ответ #8

    QUESTION_1_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-0' and not(@hidden)]"  # Сложенный ответ №1
    QUESTION_2_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-1' and not(@hidden)]"  # Сложенный ответ №2
    QUESTION_3_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-2' and not(@hidden)]"  # Сложенный ответ №3
    QUESTION_4_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-3' and not(@hidden)]"  # Сложенный ответ №4
    QUESTION_5_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-4' and not(@hidden)]"  # Сложенный ответ №5
    QUESTION_6_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-5' and not(@hidden)]"  # Сложенный ответ №6
    QUESTION_7_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-6' and not(@hidden)]"  # Сложенный ответ №7
    QUESTION_8_DROP = By.XPATH, ".//div[@aria-labelledby='accordion__heading-7' and not(@hidden)]"  # Сложенный ответ №8


class IconsLocators:

    ICON_YANDEX = By.XPATH, '//img[@alt="Yandex"]'  # Иконка Яндекс
    ICON_SCOOTER = By.XPATH, '//img[@alt="Scooter"]'  # Иконка Самокат
    MAIN_IMG = By.XPATH, ".//img[@src='/assets/scooter.png']"  # Картинка Самоката на главной странице
    ICON_DZEN = By.CLASS_NAME, "l6798a3bc"
