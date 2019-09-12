# forkit
`forkit` is a command line tool to help open source contributors get to contributing sooner.

Contributing to open source for the first time could be overwhelming. The extra work aside from programming to do in order to contribute, from installing the correct dependencies to opening a pull request, is a lot to keep in mind. The aim of this tool is to tastefully simplify these steps.

We think it's important that people learn about the underlying workflows and existing solutions; however, you shouldn't have to be a git sensei to be able to contribute.

Written in Python3.7

## Table of Contents
* [Setup](#setup)
* [Usage](#usage)
* [Features](#features)
* [Contact](#contact)

## Setup
Clone the repository:
`git clone https://github.com/samuelrey/forkit`

From within the project directory, create a file called `config.py` that should look like this:

```python
user_login=samuelrey    # your Github username
access_token=peanutbutterbattalion    # your Github access token made specifically for forkit
```

[How to generate a personal access token](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). We require `public_repo, repo:status` access.

You must do this step if you want to contribute to forkit as well.

And install with pip3:
`pip3 install .`

### Contributors
You may want to create a [virtualenv](https://virtualenv.pypa.io/en/latest/) to keep dependencies clean.

Install dependencies with:
`pip install -r requirements.txt`

## Usage
Give it a shot with:
`forkit samuelrey forkit`

You should have successfully forked this repository! :tada:

### Contributors
Try running tests with:
`python -m unittest forkit_test.py`

## Features
* Fork Github repository
* Clone the newly forked repository to the current working directory

TODO:
* Automate creation of `config.py`
* Potentially install dependencies for user

## Contact
Created by [@samuelrey](https://github.com/samuelrey) - feel free to reach out!
