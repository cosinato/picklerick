#!/usr/bin/env python3
#
import os
import sys
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


def halp(*args, **kwargs):
    print("Halp")


def hello(name: str = "World", dryrun=False):
    logging.info(f"Hello for {name}")
    print(f"Hello, {name}")


def write_git_commit_msg_template():
    with open(os.path.expanduser(COMMIT_TEMPLATE_CFGFILE), "wt") as fileio:
        fileio.write(COMMIT_TEMPLATE_MESSAGE)


def init_git(name: str = "World", dryrun=False):
    if dryrun:
        print(f"git config --global user.name {name}")
    else:
        logging.info(f"git config for {name}")
        getoutput(f"git config --global user.name {name}")


def config_git(name: str = "World", dryrun=False):
    if dryrun:
        print(f"git config --global user.name {name}")
        print(f"git config --global user.email {name}@picklerick.com")
        print("git config --global init.defaultbranch=main")
        print("git config --global commit.template ~/.config/gitmsg.txt")
    else:
        logging.info(f"git config for {name}")
        getoutput(f"git config --global user.name {name}")
        getoutput(f"git config --global user.email {name}@picklerick.com")
        getoutput("git config --global init.defaultbranch=main")
        write_git_commit_msg_template()
        getoutput("git config --global commit.template ~/.config/gitmsg.txt")


def onboarding(name: str = "World", dryrun=False):
    config_git(name=name, dryrun=dryrun)


def parse_args(argv=None):
    parsed = argparse.ArgumentParser(description="Picklerick LLC, Command Line Utility")
    parsed.add_argument(
        "--dry-run", action="store_true", help="Dry Run Mode (No Writes)"
    )

    sub_parsed = parsed.add_subparsers(
        help="sub command help",
        required=True,
        title="sub-commands",
        description="valid subcommands",
    )

    parser_hi = sub_parsed.add_parser("hello", help="Greets the user by name")
    parser_hi.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="World",
        help="First name of user",
    )
    parser_hi.set_defaults(command=hello)

    parser_onb = sub_parsed.add_parser(
        "onboarding", help="Invokes All New User Commands"
    )
    parser_onb.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="World",
        help="First name of user",
    )
    parser_onb.set_defaults(command=onboarding)

    parser_git = sub_parsed.add_parser("git", help="Invokes New User Git Configuration")
    parser_git.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="World",
        help="First name of user",
    )
    parser_git.set_defaults(command=config_git)

    parser_init = sub_parsed.add_parser("init", help="Creates a New Git Repo")
    parser_init.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="World",
        help="name of git repo",
    )
    parser_init.set_defaults(command=init_git)

    parser_help = sub_parsed.add_parser("help", help="Invokes Super Help")
    parser_help.add_argument("-n", "--name", metavar="name", type=str, default="Halp!")
    parser_help.set_defaults(command=halp)

    if parsed.parse_args(argv).name == "Halp!":
        parsed.print_help()
        sys.exit()
    return parsed.parse_args(argv)


def main():
    args = parse_args()
    args.command(name=args.name, dryrun=args.dry_run)


if __name__ == "__main__":
    main()
