Feature: acc02 - Logout
  # Enter feature description here

  Scenario: Logout
    # Enter steps here
  Given I am Logged in with 'test' and 'test123' credentials
    When I send Logout request
    Then I receive feedback that I am Logged out
    And I cannot visit my account page anymore
