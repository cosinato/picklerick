import os
from posixpath import expanduser
from behave import given, when, then, step
from subprocess import getoutput

scriptFile = "picklerick.py"


@when("we run the help command")
def step_impl(context):
    context.output = getoutput(f"python3 {scriptFile} help")


@then("we show awesome help info")
def step_impl(context):
    assert (
        context.output.splitlines()[0]
        == "usage: picklerick.py [-h] [--dry-run] {hello,onboarding,git,init,help} ..."
    )
    assert context.output.splitlines()[11] == "  {hello,onboarding,git,init,help}"
    assert (
        context.output.splitlines()[17] == "    help                Invokes Super Help"
    )


#  Scenario: run help command
#    When we run the help command
#    Then we show awesome help info


"""
usage: picklerick.py [-h] [--dry-run] {hello,onboarding,git,init,help} ...

Picklerick LLC, Command Line Utility

optional arguments:
  -h, --help            show this help message and exit
  --dry-run             Dry Run Mode (No Writes)

sub-commands:
  valid subcommands

  {hello,onboarding,git,init,help}
                        sub command help
    hello               Greets the user by name
    onboarding          Invokes All New User Commands
    git                 Invokes New User Git Configuration
    init                Creates a New Git Repo
    help                Invokes Super Help
"""
