from base_test import BaseTest
from orangehrm_login_page import LoginScreen

class TestLogin(BaseTest):       #Class chứa các test case liên quan đến trang đăng nhập.
    def test_successful_login(self):     #Test case (hàm) kiểm tra đăng nhập với thông tin hợp lệ.
        login_page = LoginScreen(self.driver)     #Tạo một đối tượng LoginPage, truyền vào self.driver (đã được khởi tạo trong BaseTest).
        login_page.enter_username("Admin")      #Nhập username "Admin".
        login_page.enter_password("admin123")   #Nhập password "admin123".
        login_page.click_login()
        print("Login Successfully!!!")