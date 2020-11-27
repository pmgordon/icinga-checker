"""Test Various API Utilities"""
# pylint: disable=no-self-use
# pylint: disable=too-few-public-methods

import os
import pytest
import git

from sample_module import api_utilities


class TestSetEnvironmentVariable():
    """Tests Catching Various Exceptions"""
    def test_set_env_variable(self, monkeypatch):
        """Test sets an environment variable for GIT_USERNAME,
           but not GIT_PAT"""

        #Setup (Set an environment variable)
        monkeypatch.setenv("GIT_USERNAME", "TestingUser")
        if "GIT_PAT" in os.environ:
            monkeypatch.delenv("GIT_PAT")

        #Test
        with pytest.raises(Exception) as ex:
            api_utilities.git_clone_repo()

        #Verify
        assert str(ex.value) == 'GIT_PAT is not set'

class TestMockGITService():
    """Mock Git Functions"""
    def test_success_git_clone_repo(self, mocker, monkeypatch):
        """Tests a successful git clone"""

        #Setup (Set an environment variables)
        monkeypatch.setenv("GIT_USERNAME", "TestingUser")
        monkeypatch.setenv("GIT_PAT", "TestingPAT")
        mocked_repo_clone = mocker.patch('git.Repo.clone_from')

        #Test
        api_utilities.git_clone_repo()

        #Verify (The two tests below are equalivilent)
        assert mocked_repo_clone.call_count == 1
        mocked_repo_clone.assert_called_once()

    def test_failed_login_git_clone_repo(self, mocker, monkeypatch):
        """Tests a successful git clone"""

        #Setup (Set an environment variables)
        monkeypatch.setenv("GIT_USERNAME", "BadUserName")
        monkeypatch.setenv("GIT_PAT", "BadPAT")
        mocker.patch('git.Repo.clone_from', side_effect=git.GitCommandError("Bad Password", -1))

        #Test For a particular exception
        with pytest.raises(git.GitCommandError):
            api_utilities.git_clone_repo()
