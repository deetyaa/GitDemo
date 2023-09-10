from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    successMessage = (By.CLASS_NAME, "alert-success")

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.successMessage)
