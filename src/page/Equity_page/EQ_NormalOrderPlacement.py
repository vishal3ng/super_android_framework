# from appium import webdriver
from src.page.common import Common_file
from appium.webdriver.webdriver import WebDriver

class Equity_order(Common_file):

    def __init__(self, driver):
        self.driver:WebDriver = driver

    def place_EqNormalOrder(self):
        # self.driver.
        pass