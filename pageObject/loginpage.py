
from utilities.lib import SelenumWrapper
from testCase.conftest import setup
import time
class LoginPage:
    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_xpath = "//button[@type='submit']"


    def __init__(self, driver):
        self.driver = driver


    # def setusername(self, username):
    #     s=SelenumWrapper(self.driver)
    #
    #
    #
    #     self.driver.find_element("id", self.textbox_username_id).clear()
    #     self.driver.find_element("id", self.textbox_username_id).send_keys(username)
    #
    #
    # def setpassword(self, password):
    #     self.driver.find_element("id", self.textbox_password_id).clear()
    #     self.driver.find_element("id", self.textbox_password_id).send_keys(password)
    #
    #
    # def clicklogin(self):
    #     self.driver.find_element("xpath",self.button_login_xpath).click()
    #
    # def cli_logout(self):
    #     self.driver.find_element("xpath","//a[text()='Logout']").click()



    def login(self,username,password):
        print(username,password)
        s=SelenumWrapper(self.driver)
        s.enter_text(self.textbox_username_id,username)


        s.enter_text(self.textbox_password_id,password)
        s.click_element(self.button_login_xpath)


