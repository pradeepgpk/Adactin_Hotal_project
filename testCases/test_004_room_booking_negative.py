import time

from pageObjects.LoginPage import Login
from pageObjects.SearchFunctionality import Search
class Test_Room_Booking:
    baseurl = "https://adactinhotelapp.com/"
    username = "pradeep15"
    password = "17bco836"


    def test_negative(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUsername(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()

        self.searchobj = Search(self.driver)
        self.searchobj.clickSearch()
        time.sleep(4)

        self.errormsg = self.searchobj.capturemsg()
        if self.errormsg == True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots/negative_room-booking.png")
            self.driver.close()
            assert False




