import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.recruitmentCandidatesAdd import AddingCandidates
from utilities.readConfig import ReadConfig
from utilities.customLogger import LogGenerator
import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_003_addingCandidates:

    logger = LogGenerator.log_generator()
    resume = "E:/orange_hrm/TestData/sample_resume.docx"

    url = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_candidates(self,setup):
        self.logger.info("*** Test_003: Started ***")
        self.driver = setup

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Login Page
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        #Add candidates
        self.ac = AddingCandidates(self.driver)

        self.ac.navigate_to_candidates()
        self.ac.click_add_button()

        self.logger.info("*** Adding Candidates details ***")
        self.ac.set_first_name("Aron")
        self.ac.set_middle_name("Finch")
        self.ac.set_last_name("Miller")

        self.email = random_generator_email() + "@gmail.com"
        self.ac.set_email(self.email)

        self.contact = random_generator_contact()
        self.ac.set_contact(self.contact)

        self.ac.set_job_vacancy("Senior QA Lead")
        self.ac.upload_resume(self.resume)
        self.ac.set_keywords("IT,Software,Selenium")
        self.ac.set_comment("comments comments comments")

        self.ac.set_month("May")
        self.ac.set_year("2022")
        self.ac.set_date("17")
        self.ac.select_checkbox()
        self.ac.click_save()

        self.msg = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='message success fadable']"))).text
        print(self.msg)

        if "Successfully Saved" in self.msg:
            assert True
            self.driver.close()
            self.logger.info("*** Candidate details added successfully ***")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"addingcandidate.png")
            self.logger.info("*** Adding candidate details unsuccessfull ***")
            self.driver.close()
            assert False

        self.logger.info("*** Test_003: Completed ***")


def random_generator_email(size=8,chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_generator_contact(size = 10,num = string.digits):
    return ''.join(random.choice(num) for n in range(size))










