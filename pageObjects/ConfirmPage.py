from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    agreeCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    successAlert = (By.CLASS_NAME, "alert-success")

    def searchCountry(self, text):
        self.driver.find_element(*ConfirmPage.country).send_keys(text)

    def getAgreeCheckBox(self):
        return self.driver.find_element(*ConfirmPage.agreeCheckbox)

    def submitPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getSuccessAlert(self):
        successAlertText = self.driver.find_element(*ConfirmPage.successAlert).text
        return successAlertText
