Feature: acc03 - Orders
  # Enter feature description here

  Scenario: Check orders
    # Enter steps here
  Given I am logged in with 'test' and 'test123' credentials
    When I navigate to my orders
    Then I see a list of my orders
    And I can open an order to see the order details
