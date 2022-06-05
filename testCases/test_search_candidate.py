import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.searchCandidates import SearchCandidates
from pageObjects.recruitmentCandidatesAdd import AddingCandidates
from utilities.readConfig import ReadConfig
from utilities.customLogger import LogGenerator
from selenium.webdriver.common.by import By

class Test_004_SearchCandidates:

    logger = LogGenerator.log_generator()
    url = ReadConfig.getUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    result_xpath = "//table[@id='resultTable']//tbody"

    @pytest.mark.regression
    def test_search_candidate(self,setup):

        self.driver = setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # LOGIN
        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        #NAVIGATING from Recruitment -> Candidates
        self.rc = AddingCandidates(self.driver)
        self.rc.navigate_to_candidates()

        # Searching candidates
        self.sc = SearchCandidates(self.driver)

        # Search by Job Title
        self.logger.info("*** 1-Search by Job Title Started***")
        self.sc.set_job_title("Sales Representative")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH,self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByJobTitle.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 1-Search by Job Title Completed ***")

        # Search by Vacancy
        self.logger.info("*** 2-Search by Vacancy Started ***")
        self.sc.set_vacancy("Senior QA Lead")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByVacancy.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 2-Search by Vacancy Completed ***")

        # Search by Hiring Manager
        self.logger.info("*** 3-Search by Hiring Manager Started ***")
        self.sc.set_hiring_manager("Dominic Chase")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByHM.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 3-Search by Hiring manager Completed ***")

        # Search by Status
        self.logger.info("*** 4-Search by Status Started ***")
        self.sc.set_status("Shortlisted")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH,self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();",scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByStatus.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 4-Search by Status Completed ***")

        # Search by Candidate Name
        self.logger.info("*** 5-Search by Candidate Name Started ***")
        self.sc.set_candidate_name("An","Anne Clinton")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByCandidateName.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 5-Search by Candidate Name completed ***")

        # Search by Keyword
        self.logger.info("*** 6-Search by Keyword Started ***")
        self.sc.set_keyword("IT")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByKeyword.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 6-Search by Keyword Completed ***")

        # Search By Date Range
        self.logger.info("*** 7- Search By Date Range Started ***")
        self.sc.set_date_from("Apr","2022","1")
        self.sc.set_date_to("May","2022","30")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchByDateRange.png")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            # self.driver.save_screenshot(".\\Screenshots\\" + "SearchByDateRange.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 7- Search By Date Range Completed ***")

        # Search by Application Method
        self.logger.info("*** 8- Search by Application Method Started ***")
        self.sc.set_application_method("Manual")
        self.sc.click_search()
        self.driver.implicitly_wait(5)

        # scrolling down page
        scroll_down = self.driver.find_element(By.XPATH, self.result_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_down)

        self.result = self.driver.find_element(By.XPATH, self.result_xpath).text
        if "No Records Found" not in self.result:
            self.logger.info("*** Records found ***")
            self.sc.click_reset()
            assert True
        else:
            self.logger.info("*** Records not Found ***")
            self.driver.save_screenshot(".\\Screenshots\\" + "SearchbyApplicationMethod.png")
            self.sc.click_reset()
            assert False
        self.logger.info("*** 8- Search by Application Method Completed ***")

        self.driver.close()
        self.logger.info("*** Test_004: Completed ***")














