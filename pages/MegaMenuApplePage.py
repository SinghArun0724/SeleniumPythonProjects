from utils.wait import wait_visible,wait_clickable
from selenium.webdriver.common.action_chains import ActionChains
from locators.MegaMenuLocators import MegaMenuAppleLocators

class MegaMenu:

    def __init__(self, driver):
        self.driver = driver 

    def hover_megaMenu(self):
        ele = wait_visible(self.driver, MegaMenuAppleLocators.MegaMenu_DropDown)
        ActionChains(self.driver).move_to_element(ele).perform()

    def open_AppleSection(self):
        AppleSection = wait_clickable(self.driver, MegaMenuAppleLocators.Apple_Btn)
        AppleSection.click()

    def GetAppleSectionText(self):
        GetAppleText = wait_visible(self.driver, MegaMenuAppleLocators.Apple_Section).text
        return GetAppleText
    
    def OpenProduct(self):
        OpenFirstItem = wait_clickable(self.driver, MegaMenuAppleLocators.Item_Name)
        OpenFirstItem.click()

