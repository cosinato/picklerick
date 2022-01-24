import os
from behave import given, when, then, step
from subprocess import getstatusoutput, getoutput

scriptFile = "picklerick.py"


@given("we have the script")
def step_impl(context):
    assert os.path.exists(scriptFile)


@when("we run the hello command")
def step_impl(context):
    context.output = getoutput(f"python3 {scriptFile} hello")


@then("we are greeted")
def step_impl(context):
    assert context.output.splitlines()[0] == "Hello, World"
