from pageObject.loginpage import LoginPage
import  os
import  logging
from utilities.readproperty import ReadConfig
from utilities.customlogger import LoggGen
from utilities.lib import SelenumWrapper
class Test_001_login:
    baseURL=ReadConfig.getapplicaionurl()
    username=ReadConfig.getuseremail()
    password = ReadConfig.getpassword()

    logger=LoggGen.loggen()



    def test_home(self,setup):

        self.logger.info("hommepage")
        s=SelenumWrapper(setup)
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        act_title=self.driver.title


        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.error("home page title is passed")

        else:
            self.driver.save_screenshot("C:/Users/shibi/PycharmProjects/pythonProject3/Screenshot/Test_homepage.png")
            self.driver.close()


            assert False



    def test_login(self,setup):
        self.logger.info("*********** verifying login test  *******")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.driver.implicitly_wait(10)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert  True

            self.logger.info("***********logintest test is passed *******")

            self.driver.close()
        else:


            self.driver.save_screenshot("C:/Users/shibi/PycharmProjects/pythonProject3/Screenshot/Test_login.png")
            self.driver.close()
            self.logger.error("***********login test is failed *******")

            assert False




