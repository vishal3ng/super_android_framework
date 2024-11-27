import logging
import time

import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from src.page.all_pages import basepage
from appium.options.common import AppiumOptions
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

logger = logging.getLogger(__name__)


class Test_equity(basepage):
    def test_first1(self):
        logger.info("from first test ")
        self.objloginpage.login()
        time.sleep(12)
        print("hello v1")
        assert False, "all pass"
        print("hello v2")


    def test_first2(self):
        self.objloginpage.login()
        time.sleep(12)
        print("hello v2")
        assert True, "all pass"
        print("hello v2")

    def test_first3(self):
        self.objloginpage.login()
        time.sleep(12)
        print("hello v2")
        assert True, "all pass"
        print("hello v2")
