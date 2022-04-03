Feature: Edit account
  # Enter feature description here

  Scenario: Edit account's details
    Given I am logged in with 'test' and 'test123' credentials
    When I navigate to the personal information page
    And I update my details
    Then I receive feedback that 'Account has been updated.'


  Scenario: Change address
    Given I am logged in with 'test' and 'test123' credentials
    When I navigate to the personal information page
    And I change my street name
    Then I receive feedback that 'Account has been updated.'