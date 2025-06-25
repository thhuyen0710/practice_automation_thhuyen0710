from selenium.webdriver.common.by import By     #Dùng để xác định cách tìm kiếm phần tử (theo xpath, id, name, class, ...)
from selenium.webdriver.support.ui import WebDriverWait     #Cho phép chờ một điều kiện nhất định xảy ra trước khi thực hiện hành động tiếp theo.   
from selenium.webdriver.support import expected_conditions as EC    #Các điều kiện mong muốn để sử dụng với WebDriverWait (ví dụ, phần tử hiển thị, có thể click, ...).

class LoginScreen: #Lớp đại diện cho trang đăng nhập
    def __init__(self, driver):     #Driver: Đối tượng WebDriver (Chrome, Firefox, ...) được truyền vào từ bên ngoài. (từ BaseTest)
        self.driver = driver    #Gán driver cho biến self.driver để có thể truy cập trong các hàm khác của class.
        self.wait = WebDriverWait(driver, 15)   #Khởi tạo một đối tượng WebDriverWait để chờ đợi các điều kiện với thời gian chờ tối đa là 15 giây.

    def enter_username(self, username):     #Hàm để nhập username vào ô username.
        username_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))   #Điều kiện là phần tử có XPATH //input[@name='username'] phải hiển thị trên trang.
        )
        username_textbox.send_keys(username)    #Sau khi tìm thấy và chắc chắn phần tử đã hiển thị, nhập giá trị username vào ô đó.

    def enter_password(self, password):     #Tương tự hàm trên
        password_textbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_textbox.send_keys(password)

    def click_login(self):      #Hàm để click vào nút đăng nhập.
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))      #Điều kiện là phần tử có XPATH //button[@type='submit'] phải có thể click được.
        )
        login_button.click()    #Sau khi tìm thấy và chắc chắn phần tử đã click được, click vào nút đó.

# Tóm tắt ý nghĩa
# Class LoginPage giúp bạn tương tác với trang đăng nhập một cách dễ dàng và có cấu trúc.
# Bạn có thể dùng class này trong các test case để thực hiện các bước đăng nhập.
# Việc sử dụng WebDriverWait giúp test ổn định hơn, tránh các lỗi do trang web chưa load xong.