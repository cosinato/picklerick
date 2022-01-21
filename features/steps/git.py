import os
from posixpath import expanduser
from behave import given, when, then, step
from subprocess import getoutput

scriptFile = "picklerick.py"
commitMesg = "~/.config/gitmsg.txt"


@when("we run the git command")
def step_impl(context):
    context.output = getoutput(f"python3 {scriptFile} --dry-run git")


@then("we configure git user info")
def step_impl(context):
    assert context.output.splitlines()[0] == "git config --global user.name World"
    assert (
        context.output.splitlines()[1]
        == "git config --global user.email World@picklerick.com"
    )
    assert (
        context.output.splitlines()[2] == "git config --global init.defaultbranch=main"
    )


@then("we configure git default template")
def step_impl(context):
    assert (
        context.output.splitlines()[3]
        == "git config --global commit.template ~/.config/gitmsg.txt"
    )
    # assert os.path.exists(expanduser(commitMesg))
