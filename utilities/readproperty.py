
import configparser
config=configparser.RawConfigParser()
config.read("C:/Users/shibi/PycharmProjects/pythonProject3/Configurations/config.ini")

class ReadConfig:
    @staticmethod
    def getapplicaionurl():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getuseremail():
        useremail = config.get("common info", "user_email")
        return useremail

    @staticmethod
    def getpassword():
        password = config.get("common info", "password")
        return  password