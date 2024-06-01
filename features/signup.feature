Feature: Check the signup functionality

  Background:
    Given login: I am an user on the login page

  @test20
  Scenario: I am trying to create a "personal" account on the page with a wrong email, then a correct email.
    When base: I click the "Sign up." button
    When signup: I click on "PERSONAL"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Paula"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Nechita"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "paula"
    Then signup: Error message is displayed with the error message: Please enter a valid email address.
    When signup: I clear the name input which was "paula"
    When signup: I fill the name input with value "nechitapaula351@yahoo.com"
    Then signup: Error message is not displayed anymore

  @test21
  Scenario: I am trying to create a "personal" account and verify if password notifications are displayed
    When base: I click the "Sign up." button
    When signup: I click on "PERSONAL"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Paula"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Nechita"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "fsdfsd@yahoo.com"
    When signup: I click on "Continue"
    Then signup: Between 8 and 72 characters notification is displayed
    Then signup: Uppercase characters notification is displayed
    Then signup: Lowercase characters notification is displayed
    Then signup: Numbers notification is displayed
    Then signup: Special characters notification is displayed

  @test22
  Scenario: I am trying to create a "business" account and verify if password notifications are displayed
    When base: I click the "Sign up." button
    When signup: I click on "BUSINESS"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "numeBusiness"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Paula"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "Nechita"
    When signup: I click on "Continue"
    When signup: I fill the name input with value "workemail@yahoo.com"
    When signup: I click on "Continue"
    Then signup: Between 8 and 72 characters notification is displayed
    Then signup: Uppercase characters notification is displayed
    Then signup: Lowercase characters notification is displayed
    Then signup: Numbers notification is displayed
    Then signup: Special characters notification is displayed
