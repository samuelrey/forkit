import github


def fork_repo(gobj, owner_login, repo_name):
    '''Fork the repository of owner/repo for the current user

    Arguments:
        gobj: A Github object used to make requests.
        owner_login: A string that represents the Github login of the owner.
        repo_name: A string that represents the Github full name of the repo.

    Returns:
        A Github Repository
    '''
    user = gobj.get_user()
    repo = gobj.get_user(owner_login).get_repo(repo_name)
    return user.create_fork(repo)


########################################
#   UNDER CONSTRUCTION                 #
########################################
def clone_repo(user, repo, git_dir=None):
    '''Clones the repository at user/repo to the target directory
    '''
    git = Git(git_dir)
    git.clone(githuburl.format(user, repo))
    return git_dir + repo


def add_upstream_remote(owner, repo, remote='upstream', git_dir=None):
    git = Git(git_dir)
    git.remote('add', remote, githuburl.format(owner, repo))


def checkout_dev_branch(branch='dev', git_dir=None):
    git = Git(git_dir)
    git.checkout(b=dev_branch)


def _get_github_object(access_token):
    return github.Github(access_token)
