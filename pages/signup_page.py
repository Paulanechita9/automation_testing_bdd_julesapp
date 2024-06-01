from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys


class SignupPage(Browser):
    SIGNUPBUTTON = (By.CLASS_NAME, 'jss17 jss91')
    PERSONAL = (By.CSS_SELECTOR, 'input[value="personal"]')
    BUSINESS = (By.CSS_SELECTOR, 'input[value="business"]')
    CONTINUE1 = (By.XPATH, '//span[normalize-space()="CONTINUE"]')
    INPUTNAME = (By.XPATH, '//input[@placeholder="Type your answer here..."]')
    ERRORMSG = (By.CSS_SELECTOR, '.MuiFormHelperText-root.MuiFormHelperText-contained.MuiFormHelperText-filled')

    def clickSignup(self):
        self.driver.find_element(*self.SIGNUPBUTTON).click()

    def clickPersonal(self):
        self.driver.find_element(*self.PERSONAL).click()

    def clickBusiness(self):
        self.driver.find_element(*self.BUSINESS).click()

    def clickContinue1(self):
        self.driver.find_element(*self.CONTINUE1).click()
        sleep(2)

    def setFirstName(self, name):
        self.driver.find_element(*self.INPUTNAME).send_keys(name)

    def displayError(self, expectedMsg):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERRORMSG).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expectedMsg == actual_message, f'Error message is incorrect, expected: {expectedMsg}, actual: {actual_message}'

    def clearNameInput(self, name):
        self.driver.find_element(*self.INPUTNAME).send_keys(Keys.BACKSPACE*len(name))
        sleep(2)

    def errorNotDisplayed(self):
        sleep(1.5)
        try:
            actual = self.driver.find_element(*self.ERRORMSG).is_displayed()
            expected = False
        except NoSuchElementException:
            actual = False
            expected = False

        assert actual == expected, f'Error message is displayed, actual: {actual}, expected: {expected}'

    def betweenPwdNotification(self):
        sleep(2)
        expected_msg = 'Between 8 and 72 characters'
        try:
            actual_message = self.driver.find_element(By.XPATH,
                                                      '//span[normalize-space()="Between 8 and 72 characters"]').text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message, (f'Password notification is displayed, expected: {expected_msg}, '
                                                f'actual: 'f'{actual_message}')

    def uppercasePwdNotification(self):
        sleep(2)
        expected_msg = 'Uppercase characters'
        try:
            actual_message = self.driver.find_element(By.XPATH, '//span[normalize-space()="Uppercase characters"]').text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message, f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def lowercasePwdNotification(self):
        sleep(2)
        expected_msg = 'Lowercase characters'
        try:
            actual_message = self.driver.find_element(By.XPATH, '//span[normalize-space()="Lowercase characters"]').text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message, f'Password notification is displayed, expected: {expected_msg}, actual: {actual_message}'

    def numbersPwdNotification(self):
        sleep(2)
        expected_msg = 'Numbers'
        try:
            actual_message = self.driver.find_element(By.XPATH, '//span[normalize-space()="Numbers"]').text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message, (f'Password notification is displayed, expected: {expected_msg}, actual:'
                                                f' {actual_message}')

    def specialPwdNotification(self):
        sleep(2)
        expected_msg = 'Special characters'
        try:
            actual_message = self.driver.find_element(By.XPATH, '//span[normalize-space()="Special characters"]').text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_msg == actual_message, (f'Password notification is displayed, expected: {expected_msg}, actual:'
                                                f' {actual_message}')
