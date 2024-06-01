from behave import *


@when('signup: I click on "PERSONAL"')
def step_impl(context):
    context.signup_page.clickPersonal()


@when('signup: I click on "Continue"')
def step_impl(context):
    context.signup_page.clickContinue1()


@when('signup: I fill the name input with value "{name}"')
def step_impl(context, name):
    context.signup_page.setFirstName(name)


@then('signup: Error message is displayed with the error message: {errorMsg}')
def step_impl(context, errorMsg):
    context.signup_page.displayError(errorMsg)


@when('signup: I clear the name input which was "{name}"')
def step_impl(context, name):
    context.signup_page.clearNameInput(name)


@when('signup: I click on "BUSINESS"')
def step_impl(context):
    context.signup_page.clickBusiness()


@then('signup: Error message is not displayed anymore')
def step_impl(context):
    context.signup_page.errorNotDisplayed()


@then('signup: Continue button is disabled')
def step_impl(context):
    context.signup_page.continueBtnEnabled()


@then('signup: Between 8 and 72 characters notification is displayed')
def step_impl(context):
    context.signup_page.betweenPwdNotification()


@then('signup: Uppercase characters notification is displayed')
def step_impl(context):
    context.signup_page.uppercasePwdNotification()


@then('signup: Lowercase characters notification is displayed')
def step_impl(context):
    context.signup_page.lowercasePwdNotification()


@then('signup: Numbers notification is displayed')
def step_impl(context):
    context.signup_page.numbersPwdNotification()


@then('signup: Special characters notification is displayed')
def step_impl(context):
    context.signup_page.specialPwdNotification()
