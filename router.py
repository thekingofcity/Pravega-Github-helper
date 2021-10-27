import re
import sys

from git import Repo

from utils import Mbox, get_issue, generate_branch_name
from constants import ISSUE_URL, WORKING_DIR, BASE_BRANCH_NAME
from startIssue import start_issue
from finishIssue import finish_issue
from cleanupIssue import cleanup_issue


def router(issue_url: str, working_dir: str = WORKING_DIR):
    issue = get_issue(issue_url)
    branch_name = generate_branch_name(issue)

    # make sure the working_dir is the repo that have this issue
    repo_name = re.match(r'https://github.com/(\S+)/(\S+)/issues/\d+',
                         issue_url)
    assert repo_name.group(2) in working_dir

    # is a valid repo
    repo = Repo(working_dir)
    assert not repo.bare

    # switch logic
    if issue['state'] == 'closed':
        cleanup_issue(issue, repo, BASE_BRANCH_NAME)
    else:
        assert issue['state'] == 'open'
        if repo.active_branch.name == branch_name:
            finish_issue(issue, repo, repo_name)
        else:
            start_issue(issue, repo, BASE_BRANCH_NAME)

if __name__ == '__main__':
    try:
        router(ISSUE_URL, WORKING_DIR)
    except (RuntimeError, AssertionError) as e:
        Mbox(type(e), str(e))
    except Exception as e:
        Mbox('Unexpected Error', str(e))
