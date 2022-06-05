import configparser

config = configparser.RawConfigParser()
config.read("E:\orange_hrm\Configurations\config.ini")    # reading data from config.ini file

class ReadConfig:

    @staticmethod
    def getUrl():
        url = config.get("input","url")
        return url

    @staticmethod
    def getUsername():
        username = config.get("input","username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("input","password")
        return password
