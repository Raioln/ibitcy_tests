from time import sleep

import allure

from selenium.webdriver import (
    Chrome,
    Remote
)
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from simple_settings import settings


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def is_initialised(cls):
        return bool(cls._instances)


class Driver(Chrome if settings.IS_LOCAL else Remote, metaclass=Singleton):

    def __init__(self, *args, **kwargs):
        if settings.IS_LOCAL:
            if 'command_executor' in kwargs.keys():
                kwargs.pop('command_executor')
            super().__init__(executable_path=settings.CHROME_DRIVER_PATH, *args, **kwargs)
        else:
            super().__init__(*args, **kwargs)

    def get_url_with_basic_auth(self, url):
        with allure.step(f'Переходим на урл : {url}'):
            super().get(f'{settings.USER_BASIC_AUTH}@{url}')
            sleep(2)

    def get_element(self, locator, wait_time=5):
        try:
            element = WebDriverWait(self, wait_time).until(
                lambda x: self.find_element(locator.by, locator.value)
            )
            return element
        except TimeoutException:
            raise NoSuchElementException(f'Не удалось найти элемент {locator.allure_name}')
