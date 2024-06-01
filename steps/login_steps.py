from behave import *


@given('login: I am an user on the login page')
def step_impl(context):
    context.login_page.gotoLoginPage()


@when('login: I fill the username with value "{user}"')
def step_impl(context, user):
    context.login_page.setUsername(user)


@when('login: I fill the password with value "{pwd}"')
def step_impl(context, pwd):
    context.login_page.setPassword(pwd)


@when('login: Leave password empty')
def step_impl(context):
    context.login_page.emptyPassword()


@when('login: Leave the username empty')
def step_impl(context):
    context.login_page.emptyUsername()


@then('login: Error message is displayed with the message: {error_message}')
def step_impl(context, error_message):
    if error_message == 'Please enter a valid email address!':
        context.login_page.display_error_message_username(error_message)
    elif error_message == 'Please enter your password!':
        context.login_page.display_error_message_password(error_message)


@then('login: Login button is disabled')
def step_impl(context):
    context.login_page.loginBtnDisabled()


@then('login: Login button is enabled')
def step_impl(context):
    context.login_page.loginBtnEnabled()
