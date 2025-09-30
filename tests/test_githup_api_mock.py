# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import unittest
from unittest.mock import patch, MagicMock
from GithubAPI567_hw3a.github_api import get_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    @patch("GithubAPI567_hw3a.github_api.requests.get")
    def test_mocked_repos_and_commits(self, mock_get):
        # Mocks response for the repo API
        mock_repos_response = MagicMock()
        mock_repos_response.status_code = 200
        mock_repos_response.json.return_value = [{"name": "mocked_repo_1"}, {"name": "mocked_repo_2"}]

        # Mocks response for commits API
        mock_commit_response = MagicMock()
        mock_commit_response.status_code = 200
        mock_commit_response.json.return_value = [{"sha": "abc123"}]

        # Side effect to return the correct mock based on URL
        def side_effect(url, *args, **kwargs):
            if "commits" in url:
                return mock_commit_response
            else:
                return mock_repos_response

        mock_get.side_effect = side_effect

        result = get_repos_and_commits("anyuser")

        # Expected output (each repo has 1 commit)
        expected = [('mocked_repo_1', 1), ('mocked_repo_2', 1)]

        self.assertEqual(result, expected)

    @patch("GithubAPI567_hw3a.github_api.requests.get")
    def test_no_repos(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = []  # no repos
        mock_get.return_value = mock_response

        result = get_repos_and_commits("anyuser")
        self.assertEqual(result, [])  # should return an empty list

    @patch("GithubAPI567_hw3a.github_api.requests.get")
    def test_failed_api_call(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        with self.assertRaises(Exception):
            get_repos_and_commits("anyuser")

if __name__ == "__main__":
    unittest.main()
