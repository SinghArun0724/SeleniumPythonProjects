from utils.basedriver import get_driver
from utils.wait import wait_clickable,wait_visible
from locators.MegaMenuLocators import MegaMenuAppleLocators
from selenium.webdriver.common.action_chains import ActionChains
from pages.MegaMenuApplePage import MegaMenu

def test_AfterHoverOpenFirstProduct():

    driver = get_driver()
    driver.get("https://ecommerce-playground.lambdatest.io/")

    Basepage = MegaMenu(driver)
    Basepage.hover_megaMenu()
    Basepage.open_AppleSection()
    Basepage.GetAppleSectionText()
    Basepage.OpenProduct

    print("Succesfully open first product")

