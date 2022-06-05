from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class SearchCandidates:

    jobtitle_drpdwn_id = "candidateSearch_jobTitle"
    vacancy_drpdwn_id = "candidateSearch_jobVacancy"
    hiringManager_drpdwn_id = "candidateSearch_hiringManager"
    status_drpdwn_id = "candidateSearch_status"
    candidateName_textbox_id = "candidateSearch_candidateName"
    candidateName_suggestions_xpath = "//div[@class='ac_results']//li"
    keyword_textbox_id = "candidateSearch_keywords"
    date_from_id = "candidateSearch_fromDate"
    date_to_id = "candidateSearch_toDate"
    applicationMethod_drpdwn_id = "candidateSearch_modeOfApplication"
    search_button_id = "btnSrch"
    reset_button_id = "btnRst"

    def __init__(self,driver):
        self.driver= driver
        self.WebDriverWait = WebDriverWait(self.driver,10)

    def set_job_title(self,value):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.ID,self.jobtitle_drpdwn_id)))
        job = Select(self.driver.find_element(By.ID,self.jobtitle_drpdwn_id))
        job.select_by_visible_text(value)

    def set_vacancy(self,value):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.ID,self.vacancy_drpdwn_id)))
        vac = Select(self.driver.find_element(By.ID,self.vacancy_drpdwn_id))
        vac.select_by_visible_text(value)

    def set_hiring_manager(self,value):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.ID,self.hiringManager_drpdwn_id)))
        hm = Select(self.driver.find_element(By.ID,self.hiringManager_drpdwn_id))
        hm.select_by_visible_text(value)

    def set_status(self,value):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.ID, self.status_drpdwn_id)))
        stat = Select(self.driver.find_element(By.ID,self.status_drpdwn_id))
        stat.select_by_visible_text(value)

    def set_candidate_name(self,letter,value):
        self.driver.find_element(By.ID,self.candidateName_textbox_id).send_keys(letter)
        self.WebDriverWait.until(EC.visibility_of_all_elements_located((By.XPATH,self.candidateName_suggestions_xpath)))
        cname = self.driver.find_elements(By.XPATH,self.candidateName_suggestions_xpath)
        for ele in cname:
            print("suggestion are:", ele.text)
            if ele.text == value:
                ele.click()
                break

    def set_keyword(self,value):
        self.driver.find_element(By.ID,self.keyword_textbox_id).send_keys(value)

    def set_date_from(self,month,year,date):

        self.driver.find_element(By.ID, self.date_from_id).click()
        select_month = Select(self.driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
        select_month.select_by_visible_text(month)

        select_year = Select(self.driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
        select_year.select_by_visible_text(year)

        alldates = self.driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']//a")
        for dateelement in alldates:
            d = dateelement.text
            if d == date:
                dateelement.click()

    def set_date_to(self,month,year,date):
        self.driver.find_element(By.ID, self.date_to_id).click()
        select_month = Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
        select_month.select_by_visible_text(month)

        select_year = Select(self.driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
        select_year.select_by_visible_text(year)

        alldates = self.driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//a")
        for dateelement in alldates:
            d = dateelement.text
            if d == date:
                dateelement.click()


    def set_application_method(self,value):
        self.WebDriverWait.until(EC.element_to_be_clickable((By.ID, self.applicationMethod_drpdwn_id)))
        am = Select(self.driver.find_element(By.ID,self.applicationMethod_drpdwn_id))
        am.select_by_visible_text(value)

    def click_search(self):
        self.driver.find_element(By.ID,self.search_button_id).click()

    def click_reset(self):
        self.driver.find_element(By.ID,self.reset_button_id).click()





