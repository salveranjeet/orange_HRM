import pytest
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGenerator
from utilities.readConfig import ReadConfig
from utilities import XLUtils

class Test_002_ddt_loginTest:

    url = ReadConfig.getUrl()
    logger = LogGenerator.log_generator()
    file = ".\\TestData\\ddt_testdata.xlsx"
    expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    @pytest.mark.regression
    def test_ddt_logintest(self,setup):
        self.logger.info("*** Test_002: DDT test Started ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.file,"Sheet1")

        self.list_status = []

        # Reading data from file
        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.file,"Sheet1",r,1)
            self.password = XLUtils.readData(self.file,"Sheet1",r,2)
            self.expected = XLUtils.readData(self.file,"Sheet1",r,3)

        # Passing data
            self.lp.set_username(self.username)
            self.lp.set_password(self.password)
            self.lp.click_login()
            self.driver.implicitly_wait(10)

            if self.driver.current_url == self.expected_url:
                if self.expected == "TC Passed":
                    self.logger.info("*** Test Passed ***")
                    self.list_status.append("Passed")
                    self.lp.click_logout()
                    self.driver.close()
                    XLUtils.writeData(self.file,"Sheet1",r,4,"As Expected")

                elif self.expected == "TC Failed":
                    self.logger.info("*** Test Failed ***")
                    self.list_status.append("Failed")
                    self.lp.click_logout()
                    self.driver.close()
                    XLUtils.writeData(self.file,"Sheet1",r,4,"Not As Expected")

            elif self.driver.current_url != self.expected_url:
                if self.expected == "TC Failed":
                    self.logger.info("*** Test Passed ***")
                    self.list_status.append("Passed")
                    self.driver.back()
                    XLUtils.writeData(self.file,"Sheet1",r,4,"As Expected")

                elif self.expected == "TC Passed":
                    self.logger.info("*** Test Failed ***")
                    self.list_status.append("Failed")
                    self.driver.back()
                    XLUtils.writeData(self.file, "Sheet1", r, 4, "Not As Expected")

        print(self.list_status)
        if "Failed" not in self.list_status:
            self.logger.info("*** Test_002: DDT Test Passed ***")
            assert True
        else:
            self.logger.info("*** Test_002: DDT Test Failed ***")
            assert False

        self.logger.info("*** Test_002: DDT Test completed")
















