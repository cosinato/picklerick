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

GIT_README_TEMPLATE = """
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)


Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started.




### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_


## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish


## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License

Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact

Your Name - - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)
"""

GIT_IGNORE_TEMPLATE = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
build/
dist/
downloads/
eggs/
.eggs/
*.egg-info/
.installed.cfg
*.egg

# Django stuff:
*.log
db.sqlite3
db.sqlite3-journal

# Environments
.env
.venv
env/
venv/
"""


def halp(*args, **kwargs):
    print("Halp")


def hello(name: str = "World", dryrun=False):
    logging.info(f"Hello for {name}")
    print(f"Hello, {name}")


def write_git_commit_msg_template():
    with open(os.path.expanduser(COMMIT_TEMPLATE_CFGFILE), "wt") as fileio:
        fileio.write(COMMIT_TEMPLATE_MESSAGE)


def makedir(path):
    if not os.path.exists(path):
        logging.info(f"creating {path}")
        try:
            os.mkdir(path)
            print(f"successfully created {path}")
        except OSError as error:
            print(f"makedir failed: {path}")
            print(error)
    else:
        print(f"path already exists: {path}")


def init_git(name: str = "project", dryrun=False):
    if not dryrun:
        makedir(name)
        if not os.path.exists(name + "/.git"):
            getoutput(f"git init {name}")
        makedir(name + "/tests")
        makedir(name + "/features")
        makedir(name + "/features/steps")

        if not os.path.exists(name + "/README.md"):
            with open(os.path.join(name, "README.md"), "wt") as fileio:
                fileio.write(GIT_README_TEMPLATE)

        if not os.path.exists(name + "/.gitignore"):
            with open(os.path.join(name, ".gitignore"), "wt") as fileio:
                fileio.write(GIT_IGNORE_TEMPLATE)
    else:
        print(f"successfully created {name}")
        print(f"successfully created {name}/tests")
        print(f"successfully created {name}/features")
        print(f"successfully created {name}/features/steps")

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
        "-p",
        "--path",
        metavar="path",
        type=str,
        default="project",
        help="path of git repo",
    )
    parser_init.add_argument(
        "-n",
        "--name",
        metavar="name",
        type=str,
        default="project",
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
