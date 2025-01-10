# Created by averkhovskaya at 1/9/25
Feature: Session 10 practice
  # Enter feature description here

  Scenario: get the weather
    Then Get weather in "San Francisco" in "metric"
    Then Get weather in "New York" in "imperial"