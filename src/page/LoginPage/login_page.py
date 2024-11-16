import time

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as we


from src.page.common import Common_file
class Loginpage(Common_file):


    def __init__(self,driver):
        self.driver:WebDriver=driver
        self.objcommon=Common_file(driver)
        self.wait=we(driver,40)

    def login(self):
        try:
            print("in mth")
            wait=we(self.driver,40)
            wait.until(EC.alert_is_present())
            self.driver.switch_to.alert.accept()
        except Exception as e:
            print(f"error {e}")
        self.click_on(self.skip_button)
        self.setValue(self.user_id, "170026")
        self.setValue(self.user_password, "170026")
        self.click_on(self.login_button)
        self.fill_otp()
        self.wait.until(EC.visibility_of(self.get_webelemet(self.cancel_biometrics)))
        self.click_on(self.cancel_biometrics)
        self.click_on(self.risk_disk_popup)

    def fill_otp(self):
        try:

            self.driver.open_notifications()
            print("notification bar open")
            self.wait.until(EC.visibility_of(self.driver.find_element(By.XPATH, self.xpathFor_OTP)))
            otp_msg = self.get_text(self.xpathFor_OTP, "text")[0:6]
            print(otp_msg)
            self.click_on(self.clearOtpNotifications)
            self.setValue(self.fill_otpxpath, otp_msg)
        except Exception:
            print("unable to set otp")
