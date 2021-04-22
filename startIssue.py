from git import Repo

from utils import Mbox, generate_branch_name


def git2master(repo: Repo) -> None:
    if repo.active_branch.name != 'master':
        if repo.is_dirty():
            selection = Mbox('Stash?',
                            'Current working directory is not clean, stash?')
            if selection:
                repo.git.stash('push', '-m', repo.active_branch)
                Mbox('Stash', f'Stash the files with name {repo.active_branch}', 0)
                return
            raise RuntimeError('Dirty repo w/o stash')
        
        repo.git.checkout('master')

def git_pull_upstream(repo: Repo) -> None:
    repo.git.pull('upstream', 'master')


def git2newbranch(repo: Repo, branch_name: str) -> None:
    repo.git.checkout('-b', branch_name)
    repo.git.push('--set-upstream', 'origin', branch_name)


def start_issue(issue: dict, repo: Repo) -> None:
    branch_name = generate_branch_name(issue)

    git2master(repo)
    assert repo.active_branch.name == 'master'
    git_pull_upstream(repo)
    git2newbranch(repo, branch_name)
