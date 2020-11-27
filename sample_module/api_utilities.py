"""Functionality that would call External APIs"""
import os
from git import Repo


def git_clone_repo():
    """Clones the Python Pytest Repo"""
    if "GIT_USERNAME" not in os.environ:
        raise Exception("GIT_USERNAME is not set")

    if "GIT_PAT" not in os.environ:
        raise Exception("GIT_PAT is not set")

    git_username = os.environ['GIT_USERNAME']
    git_access_token = os.environ['GIT_PAT']
    remote_url = (f"https://{git_username}:{git_access_token}"
                  "@github.deere.com/omops-sandbox/python-pytest-examples.git")

    full_local_path = f"{os.path.dirname(__file__)}/local_cloned_repo"

    Repo.clone_from(remote_url, full_local_path)
