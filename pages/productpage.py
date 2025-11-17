from utils.wait import wait_visible
from locators.productLocators import productLocator

class productPage:

    def __init__(self, driver):
        self.driver = driver

    def get_product_page_details(self):
        name = wait_visible(self.driver, productLocator.OpenProduct_Name).text
        price = wait_visible(self.driver, productLocator.OpenProduct_Price).text
        return name, price