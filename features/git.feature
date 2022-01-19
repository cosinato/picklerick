Feature: Configure git dev tools

  Scenario: run git config command
    When we run the git command
    Then we configure git user info
    and we configure git default template
