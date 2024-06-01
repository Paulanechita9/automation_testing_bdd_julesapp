from behave import *


@when('forgotpwd: I click the "Forgot password" button')
def step_impl(context):
    context.forgotPwd_page.clickForgotPwd()


@when('forgotpwd: I click the "Back to login" button')
def step_impl(context):
    context.forgotPwd_page.clickBackToLogin()


@when('forgotpwd: I click the "Send email" button')
def step_impl(context):
    context.forgotPwd_page.clickSendEmailBtn()


@when('forgotpwd: I fill the email with value: "{email}"')
def step_impl(context, email):
    context.forgotPwd_page.inputEmail(email)


@then('forgotpwd: The url is: "{url}"')
def step_impl(context, url):
    context.forgotPwd_page.checkURL(url)


@then('forgotpwd: Error message is displayed with the message: Please enter a valid email address!')
def step_impl(context):
    context.forgotPwd_page.errorMsg()


@then('forgotpwd: Send email button is enabled')
def step_impl(context):
    context.forgotPwd_page.sendEmailBtnEnabled()


@then('forgotpwd: Email sent notification is displayed')
def step_impl(context):
    context.forgotPwd_page.emailSentNotificationDisplayed()
