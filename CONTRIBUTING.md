# Contributing to Picklerick

[Packaging](https://test.pypi.org/project/picklerick/)  

#### 

The following is a set of guidelines for contributing to Picklerock, which is hosted in the [GitHub Repository](https://github.com/cosinato/picklerick). Feel free to propose changes to this document in a pull request.


#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Your First Code Contribution](#your-first-code-contribution)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Python Styleguide](#python-styleguide)
  * [Specs Styleguide](#specs-styleguide)
  * [Documentation Styleguide](#documentation-styleguide)


## Code of Conduct

This project and everyone participating in it is governed by . By participating, you are expected to uphold this code. Please report unacceptable behavior to [cosinato@pm.me](mailto:cosinato@pm.me).

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for Picklerick. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

> **Note:** If you find a **Closed** issue that seems like it is the same thing that you're experiencing, open a new issue and include a link to the original issue in the body of your new one.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/).

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible. For example, start by explaining how you started Picklerick, e.g. which command exactly you used in the terminal, or how you started Picklerock otherwise. When listing steps, **don't just say what you did, but explain how you did it**. 
* **Provide specific examples to demonstrate the steps**. Include links to files or GitHub projects, or copy/pasteable snippets, which you use in those examples. If you're providing snippets in the issue, use [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**
* **If the problem wasn't triggered by a specific action**, describe what you were doing before the problem happened and share more information using the guidelines below.

Provide more context by answering these questions:

* **Did the problem start happening recently** 
* **Can you reliably reproduce the issue?** If not, provide details about how often the problem happens and under which conditions it normally happens.

Include details about your configuration and environment:

* **Which version of Picklerick are you using?** You can get the exact version by running `./picklerick -V` in your terminal.
* **What's the name and version of the OS you're using**?
* **Are you running Picklerick in a virtual machine?** If so, which VM software are you using and which operating systems and versions are used for the host and the guest?

### Suggesting Enhancements


Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). Create an issue on that repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots** which help you demonstrate the the suggestion.
* **Explain why this enhancement would be useful** 
* **Specify the name and version of the OS you're using.**


### Pull Requests

Unsure where to begin contributing? You can start by looking through the issues.


## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title
* Consider starting the commit message with an applicable emoji:
    * :art: `:art:` when improving the format/structure of the code
    * :racehorse: `:racehorse:` when improving performance
    * :non-potable_water: `:non-potable_water:` when plugging memory leaks
    * :memo: `:memo:` when writing docs
    * :penguin: `:penguin:` when fixing something on Linux
    * :apple: `:apple:` when fixing something on macOS
    * :checkered_flag: `:checkered_flag:` when fixing something on Windows
    * :bug: `:bug:` when fixing a bug
    * :fire: `:fire:` when removing code or files
    * :green_heart: `:green_heart:` when fixing the CI build
    * :white_check_mark: `:white_check_mark:` when adding tests
    * :lock: `:lock:` when dealing with security
    * :arrow_up: `:arrow_up:` when upgrading dependencies
    * :arrow_down: `:arrow_down:` when downgrading dependencies
    * :shirt: `:shirt:` when removing linter warnings

### Python Styleguide

All Python code is linted with [flake8](https://flake8.pycqa.org/en/latest/user/index.html).
All Python code is formatted according to [Black](https://black.readthedocs.io/en/stable/installation_and_usage.html)


### Testing Styleguide

- Include thoughtfully-worded, well-structured scenarios in the `features` folder.


### Documentation Styleguide

* Use [Markdown](https://daringfireball.net/projects/markdown).




