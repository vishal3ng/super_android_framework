import logging
import time
import traceback
import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as we
import pytest
import configparser

from src.page.common import Common_file

logger = logging.getLogger(__name__)
class Loginpage(Common_file):

    def __init__(self, driver, device_name):
        self.driver: WebDriver = driver
        self.objcommon = Common_file(driver)
        self.wait = we(driver, 40)
        self.device_name = device_name

    id = ""
    password = ""

    def get_id_password(self):
        result=False
        try:
            data = configparser.ConfigParser()
            data.read("util/dataPrime.ini")
            self.id = data[self.device_name].get("USER_ID")
            # self.id ="170026"
            self.password = data[self.device_name].get("USER_PASSWORD")
            # self.password = "170026"
            result=True
        except Exception as e:
            assert result,"unable to get ID and password "

        return result



    def login(self):

        try:
            print("in mth")
            wait = we(self.driver, 40)
            wait.until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()

        except Exception as e:
            print(f"error {e}")
        assert self.get_id_password(),"unable to get id and pass "
        assert self.click_on(self.skip_button,"Skip button ")
        assert self.setValue(self.user_id,"User ID", self.id)
        assert self.setValue(self.user_password, "User Password ",self.password)
        assert self.click_on(self.login_button,"Login Button")
        assert self.fill_otp()
        self.wait.until(EC.visibility_of(self.get_webelemet(self.cancel_biometrics)))
        self.click_on(self.cancel_biometrics,"Cancel Biometric pop-up")
        self.click_on(self.risk_disk_popup,"Accept risk disclose pop-up")

    # @allure.step("Fill OTP from recevied SMS ")
    def fill_otp(self):
        result=False
        try:
            self.driver.open_notifications()
            print("notification bar open")
            self.wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, self.xpathFor_OTP)))
            otp_msg = self.get_text(self.xpathFor_OTP, "text")[0:6]
            # print(otp_msg)
            self.click_on(self.clearOtpNotifications,"Clear notification ")
            self.setValue(self.fill_otpxpath,"OTP", otp_msg)
            result=True
            self.allureStep(f"OTP fill successfully ")
        except Exception as e:
            self.allureStep(f"Unable to fill OTP {e}")
        return result


