import git
import github
import os.path

githuburl = 'https://github.com/{}/{}'


def get_current_login():
    import secrets
    return secrets.login


def fork_repo(gobj, owner_login, repo_name):
    '''Fork the source repository for the current user

    Arguments:
        gobj: A Github object used to make requests.
        owner_login: A string that represents the Github login of the repo
            owner.
        repo_name: A string that represents the Github full name of the repo.

    Returns:
        A Github Repository.

    Raises:
        GithubException
    '''
    user = gobj.get_user()
    repo = gobj.get_user(owner_login).get_repo(repo_name)
    return user.create_fork(repo)


def clone_repo(repo_name, owner_login=get_current_login(), project_dir='.'):
    '''Clones the repository at user/repo to the target directory

    Arguments:
        repo_name: A string that represents the Github full name of the repo.
        owner_login: A string that represents the Github login of the repo
            owner. Defaults to the current login.
        project_dir: A string that represents the filepath to an existing
            directory to where the repo will be cloned. Defaults to the
            current directory.

    Returns:
        The path to the locally cloned repository.
    '''
    g = git.Git(project_dir)
    g.clone(githuburl.format(owner_login, repo_name))
    return os.path.join(project_dir, repo_name)

########################################
#   UNDER CONSTRUCTION                 #
########################################
def add_upstream_remote(owner, repo, remote='upstream', git_dir=None):
    git = Git(git_dir)
    git.remote('add', remote, githuburl.format(owner, repo))


def checkout_dev_branch(branch='dev', git_dir=None):
    git = Git(git_dir)
    git.checkout(b=dev_branch)


def _get_github_object(access_token):
    return github.Github(access_token)

