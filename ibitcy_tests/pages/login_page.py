from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.locator import Locator


class LoginPage(BasePage):
    BASE_URL = 'ibitcy.com/interview/qa/mobile-deposit/'

    login_input = Locator(By.NAME, 'username', 'Инпут логина')
    password_input = Locator(By.NAME, 'password', 'Инпут пароля')
    submit_btn = Locator(By.XPATH, "//div[contains(@class, 'submit gold')]//a", 'Кнопка отправки формы')
    en_btn = Locator(By.LINK_TEXT, 'EN', 'Кнопка выбора языка - EN')
    ch_btn = Locator(By.LINK_TEXT, 'CH', 'Кнопка выбора языка - CH')
    ko_btn = Locator(By.LINK_TEXT, 'KO', 'Кнопка выбора языка - KO')
    ru_btn = Locator(By.LINK_TEXT, 'RU', 'Кнопка выбора языка - RU')
    hi_btn = Locator(By.LINK_TEXT, 'HI', 'Кнопка выбора языка - HI')
    forgot_pass_btn = Locator(By.XPATH, "//div[contains(@class, 'amount-inputs')]//a[contains(@class, 'forgot')]",
                              'Кнопка "Забыл пароль"')
    forgot_pass_input = Locator(By.NAME, 'forgotPass', 'Инпут ввода емейла для восстановления пароля')
    forgot_pass_send_btn = Locator(By.XPATH, "//forgot-password//button[contains(@class, 'submit gold')]",
                                   'Кнопка восстановить пароль')

    class FailAuthPopUp:
        notification_popup = Locator(By.XPATH, "//div[contains(@class, 'notification')]",
                                     'Попап нотификации')
        notification_popup_text = Locator(By.XPATH,
                                          "//div[contains(@class, 'notification')]//div[contains(@class, 'text')]",
                                          'Текст попапа')
        notification_popup_btn = Locator(By.XPATH,
                                         "//div[contains(@class, 'notification')]//div[contains(@class, 'close')]",
                                         'Кнопка попапа')
