from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestShopping(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)
        shopPage = homePage.shopItems()
        log.info("Get all card titles")
        cards = shopPage.getCardTitles()

        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Nokia Edge":
                shopPage.getCardFooters()[i].click()

        shopPage.CheckOutItems().click()
        confirmPage = shopPage.confirmCheckOut()

        log.info("Search country name with un")
        confirmPage.searchCountry(text="un")

        self.verifyLinkPresence(linkText="United States of America")

        self.driver.find_element_by_link_text("United States of America").click()
        confirmPage.getAgreeCheckBox().click()
        confirmPage.submitPurchase().click()

        successAlertText = confirmPage.getSuccessAlert()
        log.info("Text from the confirmation page" + successAlertText)

        assert ("Success! Thank you" in successAlertText)


