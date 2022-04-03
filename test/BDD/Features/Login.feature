Feature: acc01 - Login
  # Enter feature description here

  Scenario Outline: Successful Login
    # Enter steps here
  Given I am not Logged in
    And I am on the Login page
    When I enter my <username> and <password>
    And I send request to '/login/'
    Then I am Logged in.
    Examples:
      | username | password   |
      | test     | test123    |
      | postman  | postman123 |



  Scenario: Wrong username
    When I enter my 'Wrong username' and 'password'
    And I send request to '/login/'
    Then I should see 'Customer matching query does not exist.'.


  Scenario Outline: Wrong password
    When I enter my <username> and <password>
    And I send request to '/login/'
    Then I should see 'Login credentials is invalid.'.
    Examples:
      | username | password      |
      | test     | WrongPassword |
      | postman  | WrongPassword |