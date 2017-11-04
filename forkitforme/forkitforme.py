import os
import getpass
from github import Github
from git import Git


def create_fork():  # return something ??
    username = 'user'
    password = 'pass'
    githuburl = 'https://github.com/{}/{}'
    owner = 'owner'
    repo = 'repo'
    g = Github(username, password)
    user = g.get_user()
    repo = g.get_repo(githuburl.format(owner, repo))
    user.create_repo(repo)


def clone_repo():
    target_dir = '.'
    os.chdir(target_dir)
    githuburl = 'https://github.com/{}/{}'
    username = 'user'
    repo = 'repo'
    Git().clone(githuburl.format(username, repo))
    return target_dir + repo


def add_upstream_remote():  # return something ??
    repo_dir = '/path/to/repo'
    upstream_remote = 'upstream'
    url = 'owner/repo'
    repo = git.Repo(repo_dir)
    g.remote('add', upstream_remote, url)


def checkout_dev_branch():  # return something ??
    repo_dir = '/path/to/repo'
    dev_branch = 'dev'
    repo = git.Repo(repo_dir)
    repo.git.checkout(b=dev_branch)
