from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestShopping(BaseClass):

    def test_e2e(self):
        #log
        homePage = HomePage(self.driver)
        shopPage = homePage.shopItems()
        #log
        cards = shopPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            #log
            if cardText == "Nokia Edge":
                shopPage.getCardFooters()[i].click()

        shopPage.CheckOutItems().click()
        confirmPage = shopPage.confirmCheckOut()
        #log
        confirmPage.searchCountry(text="un")
        self.verifyLinkPresence(linkText="United States of America")
        self.driver.find_element_by_link_text("United States of America").click()
        confirmPage.getAgreeCheckBox().click()
        confirmPage.submitPurchase().click()
        successAlertText = confirmPage.getSuccessAlert()
        #log
        assert ("Success! Thank you" in successAlertText)


