import pytest
from selenium import webdriver
import pytest_html
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    return driver

#### methods which will get the browser from command prompt

def pytest_addoption(parser):  # this will get the value from command line
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   # This will return the browser value to the setup method
    return request.config.getoption("--browser")


### PyTest HTML report ###

def pytest_configure(config):     #adding customized information to the report
    config._metadata['Project Name'] = "Orange-HRM Automation"
    config._metadata['Module Name'] = "User"
    config._metadata['Tester'] = "Ranjeet Salve"

@pytest.mark.optionalhook
def pytest_metadata(metadata):   # to remove default arguments from the report
    metadata.pop("Java_Home",None)
    metadata.pop("Plugins",None)
    metadata.pop("Platform",None)
    metadata.pop("Package",None)
