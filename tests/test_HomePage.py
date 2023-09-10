import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log=self.getLogger()
        print("hello")
        print("welcome new world")
        homePage=HomePage(self.driver)
        log.info("first Name is"+getData["firstname"])

        log.info("Last Name is" + getData["lastname"])
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["lastname"])
        homePage.getCheckBox().click()
        log.info("gender is" + getData["gender"])
        self.selectOptionByText(homePage.getGender(),getData["gender"])

        homePage.submitForm().click()
        alertText = homePage.getSuccessMessae().text
        log.info("success messageis recived"+alertText)
        assert ("Success" in alertText)
        self.driver.refresh

    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self,request):
        return request.param