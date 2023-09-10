import time

import pytest
from selenium import webdriver
# service_obj=Service('D:/chromedriver_win32/v109/chromedriver.exe')
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass





class  TestOne(BaseClass):
    def test_e2e(self):
        log=self.getLogger()
        homePage=HomePage(self.driver)
        checkOutPage=homePage.shopItems()
        log.info("getting all the  card titles")

        cards=checkOutPage.getCardTitles()


        #self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        #products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        i=-1
        for card in cards:
            i=i+1
            cardText=card.text
            print(cardText)
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getCheckOutButton().click()
        checkOutPage.getSubmitButton().click()
        log.info("Entering Country Name as ind")
        checkOutPage.getCountryText().send_keys("ind")
        self.verifyLinkPresence("India")
        checkOutPage.getCountry().click()
        checkOutPage.getAgreeBtn().click()
        confirmPage=checkOutPage.getPurchaseBtn()
        success = confirmPage.getSuccessMessage().text
        print(success)
        log.info("Test  REcived from application is "+success)

        assert "Success! Thank you!" in success