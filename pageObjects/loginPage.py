from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username_textbox_id = "txtUsername"
    password_textbox_id = "txtPassword"
    login_button_id = "btnLogin"
    welcome_xpath = "//a[@id='welcome']"
    logout_link = "Logout"

    def __init__(self,driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver,10)

    def set_username(self,username):
        self.WebDriverWait.until(EC.presence_of_element_located((By.ID,self.username_textbox_id)))
        self.driver.find_element(By.ID,self.username_textbox_id).clear()
        self.driver.find_element(By.ID,self.username_textbox_id).send_keys(username)

    def set_password(self,password):
        self.WebDriverWait.until((EC.presence_of_element_located((By.ID,self.password_textbox_id))))
        self.driver.find_element(By.ID,self.password_textbox_id).clear()
        self.driver.find_element(By.ID,self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.WebDriverWait.until((EC.presence_of_element_located((By.ID,self.login_button_id))))
        self.driver.find_element(By.ID,self.login_button_id).click()

    def click_logout(self):
        self.WebDriverWait.until(EC.presence_of_element_located((By.XPATH,self.welcome_xpath)))
        self.driver.find_element(By.XPATH,self.welcome_xpath).click()
        self.WebDriverWait.until(EC.presence_of_element_located((By.LINK_TEXT,self.logout_link)))
        self.driver.find_element(By.LINK_TEXT,self.logout_link).click()



