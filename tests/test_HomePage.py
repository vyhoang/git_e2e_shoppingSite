import pytest

from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        log.info("First name entered: " + getData["firstname"])

        homepage.getEmail().send_keys(getData["email"])
        log.info("Email entered: " + getData["email"])

        homepage.getHomeCheckbox().click()
        self.selectOptionByTest(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()
        message = homepage.getSuccessMessage().text

        assert ("success" in message)
        self.driver.refresh()

    # load test data from Dictionary object test_homePage_data
    # @pytest.fixture(params=HomePageData.test_homePage_data)
    # def getData(self, request):
    #     return request.param

    # load test data from excel file by method getTestData
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
