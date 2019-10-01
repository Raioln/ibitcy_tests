from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.locator import Locator


class PaymentPage(BasePage):
    status_selector = Locator(By.CLASS_NAME, 'status-selector', 'Селектор статусов')
    gold_item = Locator(By.CLASS_NAME, 'gold', 'Статус Gold')
