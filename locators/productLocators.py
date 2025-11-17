from selenium.webdriver.common.by import By

class productLocator:
        OpenProduct_Name = (By.XPATH, "//div[@class='entry-content content-title ']/h1")
        OpenProduct_Price = (By.XPATH, "//div[@class='price']/h3[@data-update='price']")

        