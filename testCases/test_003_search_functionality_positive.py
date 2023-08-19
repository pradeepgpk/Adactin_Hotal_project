import time

from pageObjects.LoginPage import Login
from pageObjects.SearchFunctionality import Search
class Test_Room_Booking:
    baseurl = "https://adactinhotelapp.com/"
    username = "pradeep15"
    password = "17bco836"

    firstname = "bala"
    lastname = "kumar"
    address= "tiruppur"
    cardnumber = 4324567854325784
    cvv = 3467


    def test_positive(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.loginpageobj = Login(self.driver)
        self.loginpageobj.setUsername(self.username)
        self.loginpageobj.setPassword(self.password)
        self.loginpageobj.clickLogin()

        self.searchobj = Search(self.driver)
        self.searchobj.setLocation()
        self.searchobj.clickSearch()

        self.searchobj.selectroom()
        self.searchobj.clickcontinue()

        self.searchobj.settxtfields(self.firstname,self.lastname,
                                    self.address,self.cardnumber,self.cvv)
        self.searchobj.booknow()


        self.conformation = self.searchobj.capturemesconformation()

        if self.conformation == True:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot("screenshots/conformation_room-booking.png")
            self.driver.close()
            assert False



