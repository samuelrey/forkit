import github
import os.path
import shutil
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

    def test_clone_repo(self):
        repo_name = 'PyGithub'
        owner_login = 'PyGithub'
        expected_dir = os.path.join('.', repo_name)

        self.assertFalse(os.path.exists(expected_dir))

        local_dir = forkit.clone_repo(repo_name, owner_login)

        self.assertEqual(local_dir, expected_dir)
        self.assertTrue(os.path.exists(local_dir))

        _remove_repo_dir(local_dir)

def _remove_repo_dir(repo_dir):
    success = False

    try:
        shutil.rmtree(repo_dir)
        success = True
    except OSError as e:
        print('Error removing repo dir {}: {}'.format(
            (e.filename, e.strerror)))

    return success

