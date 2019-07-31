#!/usr/bin/env python3.7
import argparse

if __name__ == '__main__':
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
    args = parser.parse_args()

