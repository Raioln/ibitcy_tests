import allure
from hamcrest.core import assert_that
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.driver import Driver


class Locator:
    parent_element: 'WebElement' = None
    element: 'WebElement' = None
    html = None

    def __init__(self, by, value, allure_name):
        self.by = by
        self.value = value
        self.allure_name = allure_name

    def __call__(self, wait_time=10) -> 'Locator':
        self.driver = Driver()
        self.element = (self.parent_element or self.driver).get_element(self, wait_time=wait_time)
        return self

    def __repr__(self):
        repr_str = f'Локатор By: {self.by}, Value: {self.value}'
        if self.allure_name:
            repr_str += f', Allure: {self.allure_name}'
        return repr_str

    def __getattr__(self, item):
        return self.element.__getattribute__(item)

    def __getitem__(self, item):
        return self.element[item]

    def click(self):
        allure_desc = f'Нажать на {self.allure_name}'
        with allure.step(allure_desc):
            self.element.click()

    def is_displayed(self, wait_time=3):
        try:
            return self(wait_time=wait_time).element.is_displayed()
        except (NoSuchElementException, StaleElementReferenceException):
            return False

    def assert_displayed(self, wait_time=5):
        with allure.step(f'Проверить отображение {self.allure_name}'):
            assert_that(self.is_displayed(wait_time=wait_time),
                        f'Элемент {self.allure_name} не отображается на странице')

    def wait_for_displayed(self, wait_time=5, poll_frequency=0.3):
        with allure.step(f'Ожидаем что элемент {self.allure_name} появится в DOM дереве в течении {wait_time} секунд'):
            try:
                WebDriverWait(Driver(), timeout=wait_time, poll_frequency=poll_frequency).until(
                    expected_conditions.presence_of_element_located((self.by, self.value))
                )
            except TimeoutException:
                raise NoSuchElementException(
                    f'Элемент {self.allure_name} не появился в DOM дереве за {wait_time} секунд')
            return self()

    def fill(self, value):
        with allure.step(f'Заполняем поле {self.allure_name} текстом {value}'):
            self.element.send_keys(value)
