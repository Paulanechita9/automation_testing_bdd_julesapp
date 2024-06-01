from browser import Browser
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.signup_page import SignupPage
from pages.forgotPassword_page import ForgotPwdPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.base_page = BasePage()
    context.signup_page = SignupPage()
    context.forgotPassword_page = ForgotPwdPage()


def after_all(context):
    context.browser.close()
