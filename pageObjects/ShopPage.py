from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    checkOutConfirm = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooters(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def CheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def confirmCheckOut(self):
        self.driver.find_element(*CheckOutPage.checkOutConfirm).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
