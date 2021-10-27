from git import Repo

from startIssue import git2master, git_pull_upstream
from utils import generate_branch_name


def git_delete_branch(repo: Repo, branch_name: str) -> None:
    repo.git.push('-d', 'origin', branch_name)
    repo.git.branch('-D', branch_name)


def cleanup_issue(issue: dict, repo: Repo, base_branch_name: str):
    branch_name = generate_branch_name(issue)

    if repo.active_branch.name == branch_name:
        git2master(repo, base_branch_name)
    assert repo.active_branch.name != branch_name

    git_delete_branch(repo, branch_name)

    # Optional
    git_pull_upstream(repo, base_branch_name)
