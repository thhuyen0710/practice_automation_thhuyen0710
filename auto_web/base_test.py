
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        serv = Service("D:\\HuyenTT32\\Practice\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=serv)
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        request.cls.driver = self.driver
        yield
        self.driver.quit()