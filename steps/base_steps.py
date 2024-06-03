from behave import *


@when('base: I click the "{button}" button')
def step_impl(context, button):
    context.base_page.click(button)


@then('base: The url is: "{url}"')
def step_impl(context, url):
    context.base_page.checkURL(url)


@then('base: I wait "{seconds}" seconds for the page to load')
def step_impl(context, seconds):
    context.base_page.waiting(seconds)
