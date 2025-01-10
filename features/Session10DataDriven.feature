# Created by averkhovskaya at 1/6/25
Feature: Session 10 Selenium WebDriver practice with data driven scenario

  Scenario: Login to application using custom methods
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
    Then AV click on "//a[contains(text(),'Login')]" element
    Then Wait for the element with xpath "//h5" to be present
    And AV type "annaverpcs+3@gmail.com" to an element with xpath "//input[@type='text']"
    And AV type "12345678" to an element with xpath "//input[@type='password']"
    And AV click on "//button[@type='submit']" element
    Then Wait 2 seconds
    # in case if you have already at least 1 project, then you'll land on another page Profotolizer - P&L charts
    Then AV verify page title as "Profotolizer - P&L charts"
    Then Wait 1 seconds
    Then AV click on "//span[contains(text(),"Add Project")]" element
    Then Wait 1 seconds
    #Then AV verify page title as "Profotolizer - Projects"
    #Session 9
    #Then I add new project
   # | project | start_date | description | dimension | duration |
    #| first project | 2025-01-15 | This is my first project | Month | 2 Years |
   Then I add new project with "second project" and "2025-01-15" and "descriptiondsfsdfsd" and "Month" and "2 Years"

  Scenario Outline: Login to application using custom methods DD
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
    Then AV click on " //a[contains(text(),'Login')]" element
    Then Wait for the element with xpath "//h5" to be present
    And AV type "<text>" to an element with xpath "//input[@type='text']"
    And AV type "<text1>" to an element with xpath "//input[@type='password']"
    And AV click on "//button[@type='submit'] " element
    Then Wait 2 seconds
    Then AV verify page title as "<str_title1>"
    Then Wait 1 seconds
    Then AV click on "//span[contains(text(),"Add Project")]" element
    Then Wait 3 seconds
    Then I add new project with "<project_input>" and "<start_date_input>" and "<description_input>" and "<dimention_input>" and "<duration_input>"
    Examples:
      | text                   | text1    |  str_title1                |   project_input  | start_date_input | description_input   | dimention_input | duration_input |
      | annaverpcs+5@gmail.com |  12345678 |  Profotolizer - P&L charts |  second project | 2025-01-15       | descriptiondsfsdfsd | Month           | 2 Years        |
      | annaverpcs+3@gmail.com |  12345678 |  Profotolizer - P&L charts |  third project | 2025-01-16       | gdfgdgdfg | Month           | 1 Years        |
      | annaverpcs+3@gmail.com |  12345678 |  Profotolizer - P&L charts |  final project | 2025-02-15       | cvbvcbcvb | Month           | 3 Years        |
      | annaverpcs+4@gmail.com |  12345678 |  Profotolizer - Projects |  final project | 2025-02-15       | cvbvcbcvb | Month           | 3 Years        |

