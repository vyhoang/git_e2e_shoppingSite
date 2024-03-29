from selenium.webdriver.common.by import By

from pageObjects.ShopPage import CheckOutPage


class HomePage:
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    homeCheckbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CSS_SELECTOR, "[class*='alert-success'")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        shopPage = CheckOutPage(self.driver)
        return shopPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getHomeCheckbox(self):
        return self.driver.find_element(*HomePage.homeCheckbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.successMessage)