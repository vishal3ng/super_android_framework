import logging
from datetime import datetime
from typing import Dict, Any
import allure
import pytest
from allure_commons.types import AttachmentType
# from appium import webdriver
from appium.options.common import AppiumOptions
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from src.page.LoginPage.login_page import Loginpage
# -------------------------------------



import pytest

from src.page.common import Common_file


@pytest.fixture(autouse=True,scope="function")
def drivers(request):
    print("_____ start _______")
    # --------------
    global browser, driver, wait, LOGGER
    LOGGER = logging.getLogger(__name__)
    teardownTime = datetime.now()
    import time

    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "14",
        # "deviceName": "493a3b7d",
        "DeviceID":"192.168.1.101:5555",
        "appPackage": "com.icicidirect.idirectsuper",
        "appActivity": "com.icicidirect.idirectsuper.MainActivity",
        "automationName": "UiAutomator2"
    }

    options = UiAutomator2Options().load_capabilities(desired_capabilities)
    driver = webdriver.Remote("http://localhost:4723/wd/hub", options=options)
    driver.implicitly_wait(40)
    request.cls.driver = driver
    request.cls.objloginpage=Loginpage(driver)
    request.cls.objCommon_file=Common_file(driver)
    yield driver
    driver.quit()
    print("____end_____")

# --------------------------


#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture(scope="function")
# def appium_driver():
#     cap: Dict[str, Any] = {
#         'platformName': 'Android',
#         'automationName': "uiautomator2",
#         'deviceName': 'Android',
#         'appPackage': 'com.hmh.api',
#         'appActivity': '.ApiDemos',
#         'language': 'en',
#         'locale': 'US'
#     }
#
#     url = 'http://localhost:4724'
#     global driver
#     driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#     yield driver
#     driver.quit
#
#
# @pytest.fixture()
# def adding_screenshot_Fail(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="alert message1", attachment_type=AttachmentType.PNG)
#
#
# @pytest.fixture(params=['device1', 'device2'], scope="function")
# def appium_driver1(request):
#     global driver
#     if request.param == "device1":
#         cap: Dict[str, Any] = {
#             'platformName': 'Android',
#             'automationName': "uiautomator2",
#             'udid': 'emulator-5554',
#             'appPackage': 'com.hmh.api',
#             'appActivity': '.ApiDemos',
#             'language': 'en',
#             'locale': 'US'
#         }
#         url = 'http://localhost:4724'
#         driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#
#     if request.param == "device2":
#         cap: Dict[str, Any] = {
#             'platformName': 'Android',
#             'automationName': "uiautomator2",
#             'udid': 'emulator-5556',
#             'appPackage': 'com.hmh.api',
#             'appActivity': '.ApiDemos',
#             'language': 'en',
#             'locale': 'US'
#         }
#         url = 'http://localhost:4728'
#         driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#     yield driver
#     driver.quit