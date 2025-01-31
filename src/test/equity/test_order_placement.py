import logging
import time

import pytest
from selenium.webdriver.ie.webdriver import WebDriver
import allure
from src.page.all_pages import basepage
from appium.options.common import AppiumOptions
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait

# from

logger = logging.getLogger(__name__)


class Test_Equity_orderplacement(basepage):

    @pytest.mark.aqm
    def test_equityLimitBuy(self):
        self.objloginpage.login()
        print("login done ")
        with allure.step("hello vishal "):
            pass

        print("place order  ")
        print("verify same order ")
