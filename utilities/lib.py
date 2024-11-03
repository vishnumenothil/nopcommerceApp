


class SelenumWrapper:

    def __init__(self,driver):
        self.driver=driver


    def enter_text(self,locator,value):
        self.driver.find_element("id", locator).clear()
        self.driver.find_element("id", locator).send_keys(value)


    def click_element(self,log_xpath):
        self.driver.find_element("xpath",log_xpath).click()


