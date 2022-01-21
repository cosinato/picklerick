import os
from posixpath import expanduser
from behave import given, when, then, step
from subprocess import getoutput

scriptFile = "picklerick.py"


@when("we run the init command")
def step_impl(context):
    context.output = getoutput(f"python3 {scriptFile} --dry-run init")


@then("we create the repo folder")
def step_impl(context):
    assert context.output.splitlines()[0] == "successfully created project"
    assert (
        context.output.splitlines()[1]
        == "successfully created project/tests"
    )
    assert (
        context.output.splitlines()[3] == "successfully created project/features/steps"
    )

