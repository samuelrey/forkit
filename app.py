#!/usr/bin/env python3.7
import argparse
import github

from forkit import forkit
from forkit import secrets


def main():
    parser = argparse.ArgumentParser(description='Start contributing sooner. '
                                     'Use forkit to get your dev environment '
                                     'setup.')
    parser.add_argument('owner_login',
                        help='The Github login of the repo owner, eg. '
                        'samuelrey')
    parser.add_argument('repo_name',
                        help='The name of the Github repository to fork, eg. '
                        'forkit')
    parser.add_argument('--clone',
                        help='Clone the newly forked repository to the '
                        'current directory',
                        action='store_true')
    parser.add_argument('--dev',
                        help='use in place of --clone, this also clones the '
                        'repository but also sets up a feature branch for '
                        'development',
                        action='store_true')
    # TODO(sammy): add optional argument to set up secrets
    args = parser.parse_args()

    if args.clone and args.dev:
        print('Please use either --dev or --clone, not both! Get more info '
              'with --help.')
        return 1

    # TODO(sammy): hide this behind another layer
    gobj = github.Github(secrets.access_token)

    try:
        forked_repo = forkit.fork_repo(gobj, args.owner_login, args.repo_name)
    except github.GithubException as e:
        print('Something isn\'t right...')
        return 1


if __name__ == '__main__':
    main()

