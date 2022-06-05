from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class AddingCandidates:

    recruitment_menu_xpath = "//b[normalize-space()='Recruitment']"
    candidates_menu_id = "menu_recruitment_viewCandidates"
    add_button_id = "btnAdd"
    firstname_textbox_id = "addCandidate_firstName"
    middlename_textbox_id = "addCandidate_middleName"
    lastname_textbox_id = "addCandidate_lastName"
    email_textbox_id = "addCandidate_email"
    contactno_textbox_id = "addCandidate_contactNo"
    jobvacancy_drpdwn_id = "addCandidate_vacancy"
    resume_attachment_id = "addCandidate_resume"
    keywords_textbox_id = "addCandidate_keyWords"
    comment_textbox_id = "addCandidate_comment"
    date_id = "addCandidate_appliedDate"
    month_drpdwn_xpath = "//select[@class='ui-datepicker-month']"
    year_drpdwn_xpath = "//select[@class='ui-datepicker-year']"
    date_selector_xpath = "//table[@class='ui-datepicker-calendar']//a"

    consent_checkbox_id = "addCandidate_consentToKeepData"
    save_button_id = "btnSave"
    # msg_xpath = "//div[@class='message success fadable']"



    def __init__(self,driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 10)

    def navigate_to_candidates(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH,self.recruitment_menu_xpath)))
        ActionChains(self.driver).move_to_element(self.driver.find_element(By.XPATH,self.recruitment_menu_xpath))\
            .move_to_element(self.driver.find_element(By.ID,self.candidates_menu_id)).click().perform()

    def click_add_button(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID,self.add_button_id)))
        self.driver.find_element(By.ID,self.add_button_id).click()

    def set_first_name(self,fname):
        self.driver.find_element(By.ID,self.firstname_textbox_id).send_keys(fname)

    def set_middle_name(self,mname):
        self.driver.find_element(By.ID,self.middlename_textbox_id).send_keys(mname)

    def set_last_name(self,lname):
        self.driver.find_element(By.ID,self.lastname_textbox_id).send_keys(lname)

    def set_email(self,email):
        self.driver.find_element(By.ID,self.email_textbox_id).send_keys(email)

    def set_contact(self,contact):
        self.driver.find_element(By.ID,self.contactno_textbox_id).send_keys(contact)

    def set_job_vacancy(self,value):
        drpdwn = Select(self.driver.find_element(By.ID,self.jobvacancy_drpdwn_id))
        drpdwn.select_by_visible_text(value)

    def upload_resume(self,resume):
        self.driver.find_element(By.ID,self.resume_attachment_id).send_keys(resume)

    def set_keywords(self,values):
        self.driver.find_element(By.ID,self.keywords_textbox_id).send_keys(values)

    def set_comment(self,comments):
        self.driver.find_element(By.ID,self.comment_textbox_id).send_keys(comments)

    def set_month(self,month):
        self.driver.find_element(By.ID,self.date_id).click()
        select_month = Select(self.driver.find_element(By.XPATH,self.month_drpdwn_xpath))
        select_month.select_by_visible_text(month)

    def set_year(self,year):
        select_year = Select(self.driver.find_element(By.XPATH,self.year_drpdwn_xpath))
        select_year.select_by_visible_text(year)

    def set_date(self,date):
        alldates = self.driver.find_elements(By.XPATH,self.date_selector_xpath)
        for dateelement in alldates:
            d = dateelement.text
            if d == date:
                dateelement.click()


    def select_checkbox(self):
        checkbox = self.WebDriverWait.until(EC.element_to_be_clickable((By.ID,self.consent_checkbox_id)))
        checkbox.click()

    def click_save(self):
        self.driver.find_element(By.ID,self.save_button_id).click()











