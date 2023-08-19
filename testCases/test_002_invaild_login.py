from pageObjects.LoginPage import Login

class Test_login:
    baseurl = "https://adactinhotelapp.com/"
    username = "pradeep"
    password = "17bco836"


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUsername(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()

        self.targetpage=self.loginpageobj.invailLogin()
        if self.targetpage==True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots/invalid_login.png")
            self.driver.close()
            assert False



