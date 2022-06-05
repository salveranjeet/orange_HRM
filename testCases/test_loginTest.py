import pytest
from utilities.readConfig import ReadConfig
from pageObjects.loginPage import LoginPage
from utilities.customLogger import LogGenerator

class Test_001_LoginTest:

    url = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGenerator.log_generator()

    expected_url = "https://opensource-demo.orangehrmlive.com/index.php/dashboard"

    @pytest.mark.regression
    def test_verify_homePage(self,setup):
        self.logger.info("*** Test_001: Verifying homepage title ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        title = self.driver.title

        if title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("*** Homepage verification test Passed ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"homepage.png")
            self.driver.close()
            self.logger.info("*** Homepage verification test Failed ***")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*** Test_001: Login test started ***")
        self.driver = setup
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.driver.implicitly_wait(5)

        if self.driver.current_url == self.expected_url:
            assert True
            self.lp.click_logout()
            self.driver.close()
            self.logger.info("*** Login Test Passed ***")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"loginpage.png")
            self.driver.close()
            self.logger.info("*** Login Test Failed ***")
            assert False

        self.logger.info("*** Test_001: Login Test completed")









