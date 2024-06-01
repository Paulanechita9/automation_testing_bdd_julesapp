Feature: Check the forgot password functionality

  Background:
    Given login: I am an user on the login page

  @test30
  Scenario: I click the "Forgot password" button, then I click "Back to login" button
    When forgotpwd: I click the "Forgot password" button
    Then forgotpwd: The url is: "https://jules.app/forgot-password"
    When forgotpwd: I click the "Back to login" button
    Then forgotpwd: The url is: "https://jules.app/sign-in"

  @test31
  Scenario: I click the "Forget password" button, then i input an invalid email
    When forgotpwd: I click the "Forgot password" button
    When forgotpwd: I fill the email with value: "paula"
    Then forgotpwd: Error message is displayed with the message: Please enter a valid email address!

  @test32
  Scenario: I click the "Forget password" button, then i input an valid email
    When forgotpwd: I click the "Forgot password" button
    When forgotpwd: I fill the email with value: "nechitapaula351@yahoo.com"
    Then forgotpwd: Send email button is enabled
    When forgotpwd: I click the "Send email" button
    Then forgotpwd: Email sent notification is displayed