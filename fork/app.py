from github import Github

def create_fork(repo_name):
    g = Github('user', 'pass')
    user = g.get_user()
    repo = g.get_repo(repo_name)
    user.create_repo(repo)
