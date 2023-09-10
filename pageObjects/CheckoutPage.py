from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class  CheckOutPage:
    def __init__(self,driver):
        self.driver=driver


    cardTitle=(By.XPATH, "//div[@class='card h-100']")
    cardFooter =(By.XPATH, "div/button")
    checkOutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    submitButton = (By.CSS_SELECTOR, "button[class='btn btn-success']")
    countryText = (By.ID, "country")
    selectCountry=(By.LINK_TEXT, "India")
    agreeBtn=(By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn=(By.XPATH, "//input[@type='submit']")

    def  getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutButton)
    def getSubmitButton(self):
        return self.driver.find_element(*CheckOutPage.submitButton)

    def getCountryText(self):
        return self.driver.find_element(*CheckOutPage.countryText)
    def getCountry(self):
        return self.driver.find_element(*CheckOutPage.selectCountry)
    def getAgreeBtn(self):
        return self.driver.find_element(*CheckOutPage.agreeBtn)
    def getPurchaseBtn(self):
        self.driver.find_element(*CheckOutPage.purchaseBtn).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage