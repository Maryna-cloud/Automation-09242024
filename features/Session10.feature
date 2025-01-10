# Created by averkhovskaya at 1/9/25
Feature: Session 10 practice
  # Enter feature description here

 Background:
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
    Then AV click on "//a[contains(text(),'Login')]" element
    Then Wait for the element with xpath "//h5" to be present

   #Data Driven scenaro
  Scenario Outline: Login to application with valid credentials
    And AV type "<text>" to an element with xpath "//input[@type='text']"
    And AV type "<text1>" to an element with xpath "//input[@type='password']"
    And AV click on "//button[@type='submit']" element
    Then Wait 3 seconds
    Then AV verify page title as "<str_title>"
    Examples:
      | text                   |  text1    |  str_title               |
      | annaverpcs+3@gmail.com |  12345678 |  Profotolizer - P&L charts |
      | annaverpcs+4@gmail.com |  12345678 |  Profotolizer - Projects |
      | annaverpcs+5@gmail.com |  12345678 |  Profotolizer - Projects |
      | annaverpcs+5@gmail.com |  invalid |  Profotolizer - Login |
      |      |        |  Profotolizer - Login |
      | asdsddaddadsadsa |  invalid |  Profotolizer - Login |




  Scenario: get the weather
    Then Get weather in "San Francisco" in "metric"
    Then Get weather in "New York" in "imperial"