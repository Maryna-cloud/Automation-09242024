# Created by averkhovskaya at 12/18/24
# Author: Anna Verkhovskaya
# Jira ABC-123
Feature: Test login functionality

  Scenario: Login with correct username and correct password
    Given Open "https://profitolizer.com/"
    Then Verify page by title "Home - Profitolizer"
    And Click element "//a[contains(text(),'Login')]"
    Then Wait for the element with xpath "//h5" to be present
    Then Verify that xpath "//h5" should contain text "Login to Your Account"
    # fill out the form with username and password
    When Type "annaverpcs+2@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    # click on Login button
    Then Click element "//button[@type='submit']"
    Then Wait 5 seconds
    #Verification for login on P&L charts page
    Then Wait for the element with xpath "//span[contains(text(),'annaverpcs2')]" to be present
    Then Verify page by title "Profotolizer - P&L charts"
    And Verify that xpath "//span[contains(text(),'annaverpcs2')]" should contain text "annaverpcs2"
    Then Wait 5 seconds
    
