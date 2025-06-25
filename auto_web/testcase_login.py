from base_test import BaseTest
from orangehrm_login_page import LoginScreen

class TestLogin(BaseTest):       
    def test_successful_login(self):    
        login_page = LoginScreen(self.driver)     
        login_page.enter_username("Admin")     
        login_page.enter_password("admin123") 
        login_page.click_login()
        print("Login Successfully!!!")
