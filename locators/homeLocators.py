from selenium.webdriver.common.by import By

class HomeLocators:
    Top_Collection = (By.XPATH, '//div[@id="mz-product-listing-39218404"]//h3[@class="module-title"]')
    BestSeller_Tab = (By.XPATH, "//a[normalize-space(text())='Best seller']")
    Product_Name = (By.XPATH, "(//div[@class='tab-pane fade active show']//h4[@class='title'])[1]")
    Product_Price = (By.XPATH, "(//div[@class='tab-pane fade active show']//div[@class='price']//span[@class='price-new'])[1]")

