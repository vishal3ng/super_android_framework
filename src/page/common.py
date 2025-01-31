import time
from datetime import datetime
import pytest
import allure
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as we
from selenium.webdriver.common.action_chains import ActionChains as action
class Common_file:
    excelName = datetime.now().strftime("%d-%m-%Y")
    api_button = "(//android.view.View/android.widget.Button[@resource-id=''])[last()]"
    skip_button = "//android.view.View[@content-desc='Skip'] | //android.widget.ImageView[@content-desc='Get Started']"
    accept_alert = "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"
    user_id = '//android.view.View[@content-desc="User ID"]/following-sibling::android.widget.ImageView'
    user_password = "//android.widget.EditText"
    login_button = "//android.widget.Button[@content-desc='Login']"
    last_apiOnpage = "//android.view.View[contains(@content-desc,'.com')][last()]"
    first_apiOnpage = "(//android.view.View[contains(@content-desc,'.com')])[2]"
    one_apiOnpage = "//android.view.View[contains(@content-desc,'.com') or contains(@content-desc,'.net')][var]"
    apiOnpage = "//android.view.View[contains(@content-desc,'.com') or contains(@content-desc,'.net')]"
    cancel_biometrics = "//android.widget.Button[@content-desc='Cancel']"
    risk_disk_popup = '//android.widget.Button[@content-desc="Ok, Got it"]'
    Homepage_1 = '//android.widget.ImageView[contains(@content-desc,"Home")]'
    api_Show_menu = '//android.widget.Button[@content-desc="Show menu"]'
    api_Delete = '//android.widget.Button[@content-desc="Delete"]'
    api_Yes = '//android.widget.Button[@content-desc="Yes"]'
    api_Back = '//android.widget.Button[@content-desc="Back"]'
    xpathFor_OTP = "//android.widget.TextView[contains(@text,'HLbtq4KhYKi')]"
    Watchlist_tab = "//android.widget.ImageView[contains(@content-desc,'Watchlist')]"
    search_bar = "//android.view.View[@content-desc='Search & add']"
    search_bar_set_value = "//android.widget.EditText[@text='Search Name or Symbol']"
    select_script_base = "//android.view.View[contains(@content-desc,'script') and contains(@content-desc,'exe')]"
    fill_otpxpath = "//android.view.View[contains(@content-desc,'OTP')]/following-sibling::android.widget.EditText"
    order_actionxpath = "//android.widget.Button[@content-desc='action']"
    clearOtpNotifications = "//android.widget.ImageView[contains(@content-desc,'Clear all notifications')] | //android.widget.Button[contains(@content-desc,'Clear all notifications')] | //android.widget.TextView[contains(@content-desc,'Clear,Button')]"
    placement_exchange = "//android.view.View[contains(@content-desc,'exe')]"
    placement_product = "//android.view.View[contains(@content-desc,'Delivery')]"
    placement_qty = "//android.widget.EditText[1]"
    placement_price = "//android.widget.EditText[last()]"
    placement_Charges_More = "//android.widget.ImageView[@content-desc='Charges & More']"
    placement_available = "//android.view.View[@content-desc='Available Limit']"
    placement_Market_type = "//android.view.View[@content-desc='Market']"
    placement_Limit_type = "//android.view.View[@content-desc='Limit']"
    placement_more = "//android.widget.ImageView[@content-desc='Charges & More']"
    placement_day_validity = "//android.view.View[@content-desc='Day']"
    placement_less = "//android.widget.ImageView[@content-desc='Less']"
    placement_ltp = "//android.view.View[contains(@content-desc,'Price')]"
    orders_tab = "//android.widget.ImageView[contains(@content-desc,'Orders')]"
    orders_tab_pending = "//android.view.View[contains(@content-desc,'PENDING')]"




    def __init__(self,driver):
        self.driver:WebDriver=driver
        self.wait=we(driver,40)
        self.action = action(driver,10)

    def click_on(self,xpath,element_name=None):
        result = False
        try:
            self.driver.find_element(By.XPATH, xpath).click()
            result = True
            self.allureStep(f" Click on {element_name}")
        except Exception as e:
            self.allureStep(f"Unable to click on {element_name} {xpath} ")
            assert False, f" unable to click on {element_name} {xpath}"
        return result

    def setValue(self, xpath,element_name, value):
        result=False
        try:
            time.sleep(1)
            self.click_on(xpath,element_name)
            time.sleep(0.4)
            self.driver.find_element(By.XPATH, xpath).clear()
            time.sleep(0.4)
            self.driver.find_element(By.XPATH, xpath).send_keys(value)
            if self.driver.is_keyboard_shown():
                self.driver.hide_keyboard()
            time.sleep(3)
            result=True
        except Exception as e:
            self.allureStep(f" Unable to click and fill text at {element_name} {xpath} with value {value} error msg {e}")
        return result
    def scrollup_downBypixel(self,bypoint):
        # self.action.
        pass


    def get_webelemet(self, xpath):
        global wel
        try:
            wel = None
            wel = self.driver.find_element(By.XPATH, xpath)
        except Exception:
            print(f"unable to swipe {xpath}")
        return wel

    def get_text(self, xpath, atribute="content-desc"):
        global text_ofele
        try:
            text_ofele = self.driver.find_element(By.XPATH, xpath).get_attribute(atribute)
        except Exception:
            print(f"unable to get text of element {xpath}")
        # print(f"{text_ofele} text from get text ")
        return text_ofele

    @allure.step("Back to previous page")
    def goBack(self):
        self.driver.back()

        # refresh the page

    @allure.step("Refresh page")
    def refreshPage(self):
        self.driver.refresh()

    def allureStep(self, text_toPrint):
        step_time = datetime.now().strftime("%H:%M:%S")
        text = f"{text_toPrint} time:{step_time} "
        with allure.step(text):
            pass