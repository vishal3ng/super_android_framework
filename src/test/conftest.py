import base64
import logging
import os
import time
from datetime import datetime

from allure_commons.types import AttachmentType

# from appium import webdriver
from src.page.LoginPage.login_page import Loginpage
from util.capabilities_suppliers import Backbone
import subprocess
import allure
import pytest

from src.page.common import Common_file

logging.basicConfig(filename='mobile.log', filemode='w', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', force=True)

devices=None
raw_data = "report\\allureData"
final_report = "report\\allureReport"
current_dir = os.getcwd()

allure_cmd="C:\\Users\\abc\\AppData\\Roaming\\npm\\allure.cmd"
@pytest.fixture(autouse=True,scope="session")
def adb_devices():
    logging.info("session")
    global devices
    result = subprocess.run(['adb', 'devices'], capture_output=True, text=True)
    lines = result.stdout.strip().splitlines()
    devices = [line.split()[0] for line in lines[1:] if 'device' in line and 'offline' not in line]
    print(devices)
    return devices


@pytest.fixture(autouse=True,scope="function")
def drivers(request,pytestconfig):
    if hasattr(pytestconfig, "workerinput"):
        worker_id = pytestconfig.workerinput["workerid"]
        worker_index = int(worker_id.replace("gw", ""))  # Extract numeric part
    else:
        worker_index = 0
    device_name = devices[worker_index]
    print("_____ Driver start _______")
    objbb=Backbone(device_name)
    global  driver
    driver=objbb.driverFactory()
    driver.implicitly_wait(40)
    request.cls.driver = driver
    request.cls.objloginpage=Loginpage(driver,device_name)
    request.cls.objCommon_file=Common_file(driver)
    yield driver
    driver.quit()
    print("________ Driver quit _______")

# --------------------------


#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep



# @pytest.fixture()
# def adding_screenshot_Fail(request):
#     yield
#     item = request.node
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="alert message1", attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    now = datetime.now()

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield  # Run all other pytest_runtest_makereport non wrapped hooks
    result = outcome.get_result()
    # extra = getattr(result, 'extra', [])
    # html_1=f"<tr>"\
    #        f"<td class='pass pass title='passt alt='pass'><i class='mdi-action-check-circle'></i></td>"\
    #        f"<tr>"
    # extra.append(pytest_html.extras.html(html_1))
    # result.extra = extra


    print(f"result -------- {result}")
    if result.when == "call" and result.failed:
        # file_name = result.nodeid.replace("::", "_") + ".png"
        # encoded_string = base64.b64encode(driver.get_screenshot_as_png()).decode("utf-8")
        # html = f'<div style="position:relative;"><img src="data:image/png;base64,{encoded_string}" alt="screenshot" ' \
        #        f'style="width:100%;height:auto;" /><button onclick="window.close()" ' \
        #        f'style="position:absolute;top:0;right:0;z-index:9999;"</div>'
        # extra.append(pytest_html.extras.html(html))
        filenamelog = str(datetime.now().strftime("%d-%m-%Y %H_%M"))
        screen_shot_dir=os.path.join(os.getcwd(),"report\\Screenshots")
        os.makedirs(screen_shot_dir, exist_ok=True)
        screenshot_name = f"report/screenshots/{item.name}.png"
        driver.save_screenshot(screenshot_name)
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)
    # result.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Generate the Allure report after the session ends."""
    print("\nGenerating Allure Report...")
    rawd = os.path.join(current_dir, raw_data)
    finald = os.path.join(current_dir, final_report)
    os.makedirs(rawd, exist_ok=True)
    os.makedirs(finald, exist_ok=True)
    try:
        subprocess.run(
            [allure_cmd, "generate", "--single-file", rawd, "-o", finald,"--clean"], check=True)
        print(f"Allure report generated at {finald}")
    except subprocess.CalledProcessError:
        print("Failed to generate Allure report")