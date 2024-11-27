import random

from appium import webdriver
from appium.options.android import UiAutomator2Options
import random
import configparser

class Backbone:
    def __init__(self, device: str):
        self.device = device
        print("from bb init___")

    data = configparser.ConfigParser()
    data.read("util/dataPrime.ini")
    desired_capabilities = {
        "platformName": "Android",
        "newCommandTimeout": 200,
        "appPackage": "com.icicidirect.idirectsuper",
        "appActivity": "com.icicidirect.idirectsuper.MainActivity",
        "automationName": "UiAutomator2",
        "uiautomator2ServerLaunchTimeout": 20000
    }

    def driverFactory(self):
        self.desired_capabilities["deviceName"] = self.device
        self.desired_capabilities["udid"] = self.device
        self.desired_capabilities["platformVersion"] = self.data[self.device].get("platformVersion")
        self.desired_capabilities["systemPort"] = self.data[self.device].get("systemPort")
        self.port = self.data[self.device].get("appium_port")
        # print(self.desired_capabilities)
        options = UiAutomator2Options().load_capabilities(self.desired_capabilities)
        driver = webdriver.Remote("http://localhost:" + self.port + "/wd/hub", options=options)
        return driver
