from selenium.webdriver.common.by import By

class MegaMenuAppleLocators:

    MegaMenu_DropDown = (By.XPATH, "//div[@id='entry_217834']//li//span[normalize-space(text())='Mega Menu']")
    Apple_Btn = (By.XPATH, "//div[@id='entry281_216477']//a[@title='Apple']")
    Apple_Section = (By.XPATH, "//div[@id='entry_212427']/h1[@class='h4']")
    Item_Name  = (By.XPATH, "(//div[@id='entry_212439']//h4[@class='title'])[1]")
    Item_Price  = (By.XPATH, "(//div[@id='entry_212439']//div[@class='price'])[1]")


