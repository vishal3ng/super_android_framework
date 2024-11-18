import time

import pytest
from selenium.webdriver.ie.webdriver import WebDriver

from src.page.all_pages import basepage


@pytest.mark.usefixtures("drivers")
class Test_equity(basepage):

    def test_first1(self):
        self.objloginpage.login()
        time.sleep(12)

        print("hello v1")
        assert True,"all pass"
        print("hello v2")

    def test_first2(self):
        print("hello v1")
        assert True,"all pass"
        print("hello v2")