from selenium.webdriver.common.action_chains import ActionChains
from utils.wait import wait_visible, wait_clickable
from locators.homeLocators import HomeLocators

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def hover_top_Collection(self):
        target = self.driver.find_element(*HomeLocators.Top_Collection)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", 
        target)
        ele = wait_visible(self.driver, HomeLocators.Top_Collection)
        ActionChains(self.driver).move_to_element(ele).perform()

    def openBestSeller(self):
        btn = wait_clickable(self.driver, HomeLocators.BestSeller_Tab)
        btn.click()
        print("Click the open BestSeller")

    def getProductInfo(self):
        self.driver.execute_script("window.scrollBy(0,400);")
        name = wait_visible(self.driver, HomeLocators.Product_Name).text
        price = wait_visible(self.driver, HomeLocators.Product_Price).text
        return name, price

    def open_Active_Product(self):
        first_product = wait_visible(self.driver, HomeLocators.Product_Name)
        first_product.click()

