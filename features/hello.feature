Feature: The program issues a greeting

  Scenario: run hello command
    Given we have the script 
    When we run the hello command
    Then we are greeted
