
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def  get_driver(browser="chrome"):

    browser = browser.lower()

    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(executable_path="drivers/msedgedriver.exe"))

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        raise Exception(f"Browser '{browser}' is not supported!")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver