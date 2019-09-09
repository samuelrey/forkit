import click
import git
import github
import os.path

githuburl = 'https://github.com/{}/{}'


# TODO(sammy): consider changing owner_login and repo_name to options. If we
# want to support --set-user as an option, then it wouldn't make sense to be
# forced to provide a login and repo. The alternative is that we define some
# other method for setting up the config.
@click.command()
@click.argument('owner_login')
@click.argument('repo_name')
@click.option(
    '--clone',
    help='Clone the newly forked repository to the current directory',
    is_flag=True,
    default=False)
def main(owner_login, repo_name, clone):
    '''Start contributing sooner. Use forkit to setup your dev environment.

    Arguments:

        owner_login: The Github login of the repo owner, eg. samuelrey

        repo_name: The name of the Github repository to fork, eg. forkit
    '''
    print('🕑 Forking {}/{}...'.format(owner_login, repo_name))
    gobj = github.Github(get_access_token())
    repo = fork_repo(gobj, owner_login, repo_name)
    print('🎉 Forked to {}/{}!'.format(get_current_login(), repo_name))

    if clone:
        print('🕑 Cloning {}/{}...'.format(get_current_login(), repo_name))
        local_repo = clone_repo(repo)
        if os.path.exists(local_repo):
            print('🎉 Cloned to {}!'.format(local_repo))


def get_access_token():
    import config
    return config.access_token


def get_current_login():
    import config
    return config.login


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


def clone_repo(repo, project_dir='.'):
    '''Clones the repository at the given URL to the target directory

    Arguments:
        repo: A Github repository.
        project_dir: A string that represents the filepath to an existing
            directory to where the repo will be cloned. Defaults to the
            current directory.

    Returns:
        The path to the locally cloned repository.
    '''
    g = git.Git(project_dir)
    g.clone(repo.git_url)
    return os.path.join(project_dir, repo.name)


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

