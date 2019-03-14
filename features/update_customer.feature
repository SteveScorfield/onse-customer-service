Feature: Update Customer Name

  Scenario: We need to be able to update a customers name
    Given customer "Nicole Forsgren" with ID "12345" exists
    When the customer "12345" changes their name to "Nicole Smith"
    Then customer "12345" should be "Nicole Smith"
