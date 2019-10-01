import json
import logging
import os

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.common.exceptions import WebDriverException
from simple_settings import settings
from utils.helpers import capabilities_for_browser_name
from utils.driver import Driver

if not os.path.exists('tmp'):
    os.makedirs('tmp')


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=settings.BROWSER)


@pytest.fixture(autouse=True)
def driver(request):
    browser = request.config.getoption('--browser')
    desired_capabilities = capabilities_for_browser_name(browser)

    test_name = f'{request.node.location[0]}::{request.node.location[2].replace(".", "::")}'
    desired_capabilities['name'] = test_name
    desired_capabilities['enableVNC'] = True

    remote_driver = Driver(command_executor=settings.REMOTE_URL, desired_capabilities=desired_capabilities)
    remote_driver.set_window_size(1920, 1080)

    yield remote_driver

