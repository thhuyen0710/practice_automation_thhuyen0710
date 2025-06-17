import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print(f"\nURL: {self.driver.current_url}")
        request.cls.driver = self.driver
        yield
        self.driver.quit()

class TestWebLogin(BaseTest):
    def test_login_valid(self):
        driver = self.driver
        wait = WebDriverWait(driver, 15)
        username_textbox = wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_textbox.send_keys("Admin")
        password_textbox = wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_textbox.send_keys("admin123")
        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        login_button.click()
        time.sleep(5)
        try:
            dashboard_header_selector = ".oxd-topbar-header-title"
            dashboard_header_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, dashboard_header_selector))
            )
            assert dashboard_header_element.text == "Dashboard", \
                f"Expected dashboard header text 'Dashboard', but got '{dashboard_header_element.text}'"
            print("Login successful!")

        except Exception as e:
            print(f"Login fail!: {e}")
            pytest.fail(f"Cannot verify Dashboard screen. Error: {e}")