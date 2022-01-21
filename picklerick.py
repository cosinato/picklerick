#!/usr/bin/env python3
#
import os
import argparse
import logging
from subprocess import getoutput

logging.basicConfig(
    filename="picklerick.log",
    format="[%(asctime)s]: %(message)s",
    encoding="utf-8",
    level=logging.DEBUG,
)

__version__ = "0.2.1"
COMMIT_TEMPLATE_CFGFILE = "~/.config/gitmsg.txt"
COMMIT_TEMPLATE_MESSAGE = """
Subject line (try to keep under 50 characters)

Multi-line description of commit,
feel free to be detailed.

[Ticket: X]
"""


def hello(username: str = "World", dryrun=False):
    logging.info(f"Hello for {username}")
    print(f"Hello, {username}")


def write_git_commit_msg_template():
    with open(os.path.expanduser(COMMIT_TEMPLATE_CFGFILE), "wt") as fileio:
        fileio.write(COMMIT_TEMPLATE_MESSAGE)


def config_git(username: str = "World", dryrun=False):
    if dryrun:
        print(f"git config --global user.name {username}")
        print(f"git config --global user.email {username}@picklerick.com")
        print("git config --global init.defaultbranch=main")
        print("git config --global commit.template ~/.config/gitmsg.txt")
    else:
        logging.info(f"git config for {username}")
        getoutput(f"git config --global user.name {username}")
        getoutput(f"git config --global user.email {username}@picklerick.com")
        getoutput("git config --global init.defaultbranch=main")
        write_git_commit_msg_template()
        getoutput("git config --global commit.template ~/.config/gitmsg.txt")


def onboarding(username: str = "World", dryrun=False):
    config_git(username, dryrun=dryrun)


def parse_args(argv=None):
    parsed = argparse.ArgumentParser(description="Picklerick LLC, Command Line Utility")
    parsed.add_argument("--dry-run", action="store_true", help="Dry Run Helper")

    sub_parsed = parsed.add_subparsers(
        help="command helper", required=True, title="commands"
    )

    parser_hi = sub_parsed.add_parser("hello", help="hello helper")
    parser_hi.add_argument("-n", "--name", metavar="name", type=str, default="World")
    parser_hi.set_defaults(command=hello)

    parser_onb = sub_parsed.add_parser("onboarding", help="onboarding helper")
    parser_onb.add_argument("-n", "--name", metavar="name", type=str, default="World")
    parser_onb.set_defaults(command=onboarding)

    parser_git = sub_parsed.add_parser("git", help="git helper")
    parser_git.add_argument("-n", "--name", metavar="name", type=str, default="World")
    parser_git.set_defaults(command=config_git)

    return parsed.parse_args(argv)


def main():
    args = parse_args()
    args.command(username=args.name, dryrun=args.dry_run)


if __name__ == "__main__":
    main()
