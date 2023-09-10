from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self,driver):
        self.driver=driver

    shop=(By.CSS_SELECTOR,"a[href*='shop']")
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.NAME, "email")
    checkBox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    formBtn = (By.CSS_SELECTOR, "[value='Submit']")
    successMsg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def  shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.formBtn)

    def getSuccessMessae(self):
        return self.driver.find_element(*HomePage.successMsg)
