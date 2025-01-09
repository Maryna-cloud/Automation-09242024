# Created by averkhovskaya at 1/6/25
Feature: Session 9 Selenium WebDriver practice
  Background:
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
    Then AV click on "//a[contains(text(),'Login')]" element
    Then Wait for the element with xpath "//h5" to be present

  Scenario: Login to application with valid credentials

    And AV type "annaverpcs+3@gmail.com" to an element with xpath "//input[@type='text']"
    And AV type "12345678" to an element with xpath "//input[@type='password']"
    And AV click on "//button[@type='submit']" element
    Then Wait 3 seconds
    Then AV verify page title as "Profotolizer - Projects"


  Scenario: Login to application with invalid credentials

    And AV type "annaverpcs+4@gmail.com" to an element with xpath "//input[@type='text']"
    And AV type "12345678" to an element with xpath "//input[@type='password']"
    And AV click on "//button[@type='submit']" element
    Then Wait 3 seconds
    Then AV verify page title as "Profotolizer - Login"
    #NEED to add verification for negative scenario
