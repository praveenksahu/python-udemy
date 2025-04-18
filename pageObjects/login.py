from selenium.webdriver.common.by import By

from pageObjects.shop import ShopPage
from utils.commonfunctions import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signIn = (By.ID, "signInBtn")


    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.signIn).click()

        shop_page = ShopPage(self.driver)
        return shop_page