from selenium.webdriver.common.by import By

class Search:
    drp_location_xpath = "//select[@id='location']"
    select_location_xpath = "//option[text()='Sydney']"

    btn_search_xpath = "//input[@id='Submit']"

    msg_error_xpath = "//span[@id='location_span']"

    rad_room_xpath = "//input[@id='radiobutton_1']"

    btn_continue_xpath = "//input[@id='continue']"

    txt_firstname_xpath = "//input[@id='first_name']"

    txt_lastname_xpath = "//input[@id='last_name']"

    txt_billing_address_xpath = "//textarea[@id='address']"

    txt_creditcard_number_xpath = "//input[@id='cc_num']"

    drp_card_type_xpath = "//select[@id='cc_type']"
    select_card_type_xpath = "//option[@value='VISA']"

    drp_expirymonth_xpath = "//select[@id='cc_exp_month']"
    select_month_xpath = "//option[@value='2']"

    drp_expiryyear_xpath = "//select[@id='cc_exp_year']"
    select_year_xpath = "//option[@value='2030']"

    txt_cvv_xpath = "//input[@id='cc_cvv']"

    btn_bookNow_xpath = "//input[@id='book_now']"

    msg_conformation_xpath = "//td[contains(text(),'Booking Confirmation')]"



    def __init__(self,driver):
        self.driver = driver

    def setLocation(self):
        self.driver.find_element(By.XPATH,self.drp_location_xpath).click()
        self.driver.find_element(By.XPATH,self.select_location_xpath).click()

    def clickSearch(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()

    def capturemsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.msg_error_xpath).is_displayed()
        except:
            return False

    def selectroom(self):
        self.driver.find_element(By.XPATH,self.rad_room_xpath).click()

    def clickcontinue(self):
        self.driver.find_element(By.XPATH,self.btn_continue_xpath).click()

    def settxtfields(self,firstname,lastname,address,cardnumber,cvvnumber):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(firstname)
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lastname)
        self.driver.find_element(By.XPATH,self.txt_billing_address_xpath).send_keys(address)
        self.driver.find_element(By.XPATH,self.txt_creditcard_number_xpath).send_keys(cardnumber)
        self.driver.find_element(By.XPATH,self.drp_card_type_xpath).click()
        self.driver.find_element(By.XPATH,self.select_card_type_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_expirymonth_xpath).click()
        self.driver.find_element(By.XPATH,self.select_month_xpath).click()
        self.driver.find_element(By.XPATH,self.drp_expiryyear_xpath).click()
        self.driver.find_element(By.XPATH,self.select_year_xpath).click()
        self.driver.find_element(By.XPATH,self.txt_cvv_xpath).send_keys(cvvnumber)

    def booknow(self):
        self.driver.find_element(By.XPATH,self.btn_bookNow_xpath).click()


    def capturemesconformation(self):
        try:
            return  self.driver.find_element(By.XPATH,self.msg_conformation_xpath).is_displayed()
        except:
            return False


