  # Created by averkhovskaya at 1/6/25
  @sanity @teamsept2024
  Feature: Session 8 Selenium WebDriver practice
  @smoke
  Scenario: Scenario 1
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
  @regression @sanity
  Scenario: Scenario 2
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"
  @smoke @regression
  Scenario: Scenario 3
    Given I would like to open "Provitolizer" page
    Then AV verify page title as "Home - Profitolizer"