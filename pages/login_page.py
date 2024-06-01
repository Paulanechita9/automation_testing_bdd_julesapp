from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from browser import Browser
from time import sleep
from selenium.webdriver.common.keys import Keys


class LoginPage(Browser):
    USERNAME = (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[placeholder="Enter your password"]')
    LOGIN_BTN = (By.CLASS_NAME, 'MuiButton-label')
    ERROR_MESSAGE_PASSWORD = (By.XPATH, '//p[normalize-space()="Please enter your password!"]')
    ERROR_MESSAGE_USERNAME = (By.XPATH, '//p[@class="MuiFormHelperText-root MuiFormHelperText-contained"]')

    def gotoLoginPage(self):
        self.driver.get('https://jules.app/sign-in')

    def setUsername(self, user):
        self.driver.find_element(*self.USERNAME).send_keys(user)

    def setPassword(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def emptyPassword(self):
        self.driver.find_element(*self.PASSWORD).send_keys('s')
        sleep(1)
        self.driver.find_element(*self.PASSWORD).send_keys(Keys.BACKSPACE)
        sleep(2)

    def emptyUsername(self):
        self.driver.find_element(*self.USERNAME).send_keys('s')
        sleep(1)
        self.driver.find_element(*self.USERNAME).send_keys(Keys.BACKSPACE)
        sleep(2)

    def clickLoginButton(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def display_error_message_password(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_PASSWORD).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_message == actual_message, f'Error message is incorrect, expected {expected_message}, actual {actual_message}'

    def display_error_message_username(self, expected_message):
        sleep(2)
        try:
            actual_message = self.driver.find_element(*self.ERROR_MESSAGE_USERNAME).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_message == actual_message, f'Error message is incorrect, expected {expected_message}, actual {actual_message}'

    def loginBtnDisabled(self):
        sleep(1)
        actual = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').is_enabled()
        expected = False
        assert expected == actual, f'Login button is working, expected {expected}, actual {actual}'

    def loginBtnEnabled(self):
        sleep(1)
        actual = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').is_enabled()
        expected = True
        assert expected == actual, f'Login button is not working, expected {expected}, actual {actual}'
