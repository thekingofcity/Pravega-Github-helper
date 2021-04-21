import re
import webbrowser

from git import Repo


def git_commit(repo: Repo, commit_message: str) -> None:
    repo.git.add('.')
    repo.git.commit('-s', '-m', commit_message)


def git_push(repo: Repo) -> None:
    origin = repo.remote(name='origin')
    origin.push()


def open_pullrequest(repo_name: str, branch_name: str) -> None:
    url = f'https://github.com/{repo_name}/compare/master...thekingofcity:{branch_name}'
    webbrowser.open(url)


def finish_issue(issue: dict, repo: Repo, repo_name: re.Match):
    title: str = issue['title']
    number: int = issue['number']
    branch_name = f"issue-{number}-{'-'.join(title.split(' '))}"

    # make sure the branch corresponds to the issue
    assert repo.active_branch.name == branch_name

    # make sure there is something to commit
    assert repo.is_dirty() or repo.untracked_files

    commit_message = f'[Issue-{number}] {title}'

    git_commit(repo, commit_message)
    git_push(repo)
    open_pullrequest(f'{repo_name.group(1)}/{repo_name.group(2)}', branch_name)
