from selenium.webdriver.common.by import By

class Login():
    txt_user_Name= "username"
    txt_password_Name = "password"
    btn_login_Name= "login"
    msg_myaccount_xpath = "//td[normalize-space()='Welcome to Adactin Group of Hotels']"
    msg_invaildlogin_xpath = "//b[contains(text(),'Invalid Login details or Your Password might have ')]"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.NAME,self.txt_user_Name).send_keys(username)

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME,self.txt_password_Name).send_keys(pwd)

    def clickLogin(self):
        self.driver.find_element(By.NAME,self.btn_login_Name).click()

    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False

    def invailLogin(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_invaildlogin_xpath).is_displayed()
        except:
            return False
