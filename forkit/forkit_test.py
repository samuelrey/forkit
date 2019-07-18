import github
import unittest

import forkit.forkit as forkit


class ForkitTest(unittest.TestCase):
    def setUp(self):
        import secrets
        access_token = secrets.access_token
        self.login = secrets.login
        self.g = github.Github(access_token)

    def test_fork_repo(self):
        # Should succeed given valid credentials and owner/repo.
        # Note that this will also succeed if the forked repo already exists.
        owner_login = 'PyGithub'
        repo_name = 'PyGithub'

        repo = forkit.fork_repo(self.g, owner_login, repo_name)

        self.assertEqual(repo.owner.login, self.login)
        self.assertEqual(repo.name, repo_name)
        self.assertEqual(repo.source.owner.login, owner_login)
