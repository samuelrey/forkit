import github
import os.path
import shutil
import unittest

import forkit


class ForkitTest(unittest.TestCase):
    def setUp(self):
        import config
        access_token = config.access_token
        self.login = config.login
        self.gobj = github.Github(access_token)

    def test_fork_repo(self):
        # fork_repo succeeds when current user is authorized and Github repo
        # exists.
        # Note that this will also succeed if the forked repo already exists.
        # This test should suffice to cover both cases. Another deciding
        # factor is that is that to reset the user's state on Github, ie
        # delete any repositories generated by testing, requires more
        # permissions.
        owner_login = 'PyGithub'
        repo_name = 'PyGithub'

        repo = forkit.fork_repo(self.gobj, owner_login, repo_name)

        self.assertEqual(repo.owner.login, self.login)
        self.assertEqual(repo.name, repo_name)
        self.assertEqual(repo.source.owner.login, owner_login)

        # fork_repo fails when current user is not authenticated
        unauth_gobj = github.Github('spoof access token')

        with self.assertRaises(github.GithubException):
            forkit.fork_repo(unauth_gobj, owner_login, repo_name)

        # fork_repo fails when owner cannot be found
        missing_owner_login = 'spoof owner name'

        with self.assertRaises(github.GithubException):
            forkit.fork_repo(self.gobj, missing_owner_login, repo_name)

        # fork_repo fails when repo cannot be found for an existing owner
        missing_repo_name = 'spoof repo name'

        with self.assertRaises(github.GithubException):
            forkit.fork_repo(self.gobj, owner_login, missing_repo_name)

    def test_clone_repo(self):
        repo = self.gobj.get_repo('PyGithub/PyGithub')
        expected_dir = os.path.join('.', repo.name)

        self.assertFalse(os.path.exists(expected_dir))

        local_dir = forkit.clone_repo(repo)

        self.assertEqual(local_dir, expected_dir)
        self.assertTrue(os.path.exists(local_dir))

        _remove_local_repo(local_dir)

def _remove_local_repo(repo_dir):
    success = False

    try:
        shutil.rmtree(repo_dir)
        success = True
    except OSError as e:
        print('Error removing repo dir {}: {}'.format(
            (e.filename, e.strerror)))

    return success

