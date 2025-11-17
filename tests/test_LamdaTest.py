from utils.basedriver import get_driver
from pages.homepage import HomePage
from pages.productpage import productPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_product_validation():

    driver = get_driver()
    driver.get("https://ecommerce-playground.lambdatest.io/")

    home = HomePage(driver)
    product_page = productPage(driver)

    home.hover_top_Collection()
    home.openBestSeller()

    product_name, product_price = home.getProductInfo()
    home.open_Active_Product()

    final_name, final_price = product_page.get_product_page_details()

    assert product_name == final_name, "Product name mismatch"
    assert product_price == final_price, "Product price mismatch"

    print("Validation Succesful")
