
Feature: example

  Scenario: First scenario
    Given Open "https://www.google.com"
    Then Wait 1 seconds

   Scenario: Google search verification
     Given Open "https://www.google.com"
     Then Verify page by title "Google"
     And Verify presents of element "//textarea[@name='q']"
     When Type "Python" into "//textarea[@name='q']"
     Then Click element "(//input[@name='btnK'])[1]"
     Then Wait 3 seconds
     And Verify that xpath "//textarea[@id='APjFqb']" should contain text "Python"
     # Then Wait 10 seconds
     
