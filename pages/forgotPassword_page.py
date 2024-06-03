from selenium.common import NoSuchElementException
from browser import Browser
from selenium.webdriver.common.by import By
from time import sleep


class ForgotPwdPage(Browser):
    FORGOTPWDBTN = (By.LINK_TEXT, 'Forgot password?')
    BACKTOLOGINBTN = (By.LINK_TEXT, 'Back to login')
    EMAILINPUT = (By.XPATH, '//input[@placeholder="Enter your email"]')
    INVALIDEMAILERROR = (By.CSS_SELECTOR, '.MuiFormHelperText-root.MuiFormHelperText-contained')
    SENDEMAILBTN = (By.CLASS_NAME, 'css-17qmje5')
    EMAILSENTNOTIFICATION = (By.XPATH, '//span[contains(text(),"If you have an account registered with this email ")]')

    def clickForgotPwd(self):
        self.driver.find_element(*self.FORGOTPWDBTN).click()

    def clickBackToLogin(self):
        self.driver.find_element(*self.BACKTOLOGINBTN).click()

    def checkURL(self, url):
        if url == 'https://jules.app/forgot-password':
            actual = self.driver.current_url
            expected = 'https://jules.app/forgot-password'
            assert actual == expected, f'The current URL is wrong, actual: {actual}, expected: {expected}'

        elif url == 'https://jules.app/sign-in':
            actual = self.driver.current_url
            expected = 'https://jules.app/sign-in'
            assert actual == expected, f'The current URL is wrong, actual: {actual}, expected: {expected}'

    def inputEmail(self, email):
        self.driver.find_element(*self.EMAILINPUT).send_keys(email)

    def errorMsg(self):
        expected_message = 'Please enter a valid email address!'
        try:
            actual_message = self.driver.find_element(*self.INVALIDEMAILERROR).text
        except NoSuchElementException:
            actual_message = 'None'

        assert expected_message == actual_message, f'Error message is incorrect, expected {expected_message}, actual {actual_message}'

    def sendEmailBtnEnabled(self):
        actual = self.driver.find_element(*self.SENDEMAILBTN).is_enabled()
        expected = True
        assert expected == actual, f'Send email button is disabled, expected: {expected}, actual: {actual}'

    def clickSendEmailBtn(self):
        self.driver.find_element(*self.SENDEMAILBTN).click()

    def emailSentNotificationDisplayed(self):
        actual = self.driver.find_element(*self.EMAILSENTNOTIFICATION).is_displayed()
        expected = True
        assert expected == actual, f'Notification is not displayed, expected: {expected}, actual: {actual}'
