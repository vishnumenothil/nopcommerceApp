from pageObject.loginpage import LoginPage
import  os
import  logging
from utilities.readproperty import ReadConfig
from utilities.customlogger import LoggGen
from utilities import xlutility
from utilities.lib import SelenumWrapper
import time

class Test_002_DDT_login:
    # baseURL=ReadConfig.getapplicaionurl()

    path='C://Users//shibi//PycharmProjects//pythonProject3//TestData//LoginData.xlsx'
    logger=LoggGen.loggen()



    def test_login(self,setup):
        s=SelenumWrapper(setup)
        self.logger.info("*********** verifying login test  *******")

        self.driver=setup
        # self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)

        self.rows = xlutility.getRowCount(self.path,'Sheet1')
        print(f"number of rows{self.rows}")



        list_str=[]
        for r in range(2,self.rows+1):
            self.user=xlutility.readData(self.path,'Sheet1',r,1)
            self.password = xlutility.readData(self.path, 'Sheet1', r, 2)
            self.exp=xlutility.readData(self.path, 'Sheet1', r,3)
            print(self.user)
            print(self.password)

            # self.lp.setusername(self.user)
            # self.lp.setpassword(self.password)
            # self.lp.clicklogin()
            self.lp.login(self.user,self.password)

            time.sleep(5)

            act_title=self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title  :
                if self.exp=="Pass":
                   self.logger.info("***********pass******")
                   # self.lp.cli_logout()
                   list_str.append('pass')

                elif self.exp == 'Fail':
                    self.logger.info("****fail******")
                    # self.lp.cli_logout()
                    list_str.append('fail')


            elif act_title != exp_title  :
                if self.exp == "Pass":
                    self.logger.info("***********fail******")
                    list_str.append('fail')
                    # self.lp.cli_logout()


                    list_str.append('fail')
                elif self.exp=='fail':
                    self.logger.info("***********pass*****")
                    # self.lp.cli_logout()

                    list_str.append("pass")
                    # self.driver.save_screenshot(
                    #     "C:/Users/shibi/PycharmProjects/pythonProject3/Screenshot/Test_login.png")
        print(list_str)
        if 'fail' not in list_str:
            self.logger.info("login ddt test is passed")
            print("passed")
            assert True
        else:
            self.logger.info("login ddt test faied")
            assert False


        self.logger.info("***end of login ddt test")
        self.logger.info("********** complete tc_loginDD_002*****")




