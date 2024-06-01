Feature: Check the login functionality

  Background:
    Given login: I am an user on the login page

  @test1
  Scenario: Try to login without password, only email
    When login: I fill the username with value "nechitapaula351@yahoo.com"
    When login: Leave password empty
    Then login: Error message is displayed with the message: Please enter your password!
    Then login: Login button is disabled

  @test2
  Scenario: Try to login without email, only password
    When login: I fill the password with value "parola123"
    When login: Leave the username empty
    Then login: Error message is displayed with the message: Please enter a valid email address!
    Then login: Login button is disabled

  @test3
  Scenario: Leave both the email and password empty
    When login: Leave the username empty
    When login: Leave password empty
    Then login: Error message is displayed with the message: Please enter a valid email address!
    Then login: Error message is displayed with the message: Please enter your password!
    Then login: Login button is disabled

  @test4
  Scenario: Both the email and password are correct, but unregistered, not clicking the login button
    When login: I fill the username with value "nechitapaula351@yahoo.com"
    When login: I fill the password with value "parola123"
    Then login: Login button is enabled
