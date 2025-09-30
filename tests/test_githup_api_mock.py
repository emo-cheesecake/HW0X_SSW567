# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import unittest
from unittest.mock import patch, MagicMock
from GithubAPI567_hw3a.github_api import get_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    @patch("GithubAPI567_hw3a.github_api.requests.get")
    def test_mocked_api(self, mock_get):
        # Mocked response for the repos API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"name": "mocked_repo_1"},
            {"name": "mocked_repo_2"}
        ]

        # When commits are requested, return a fake commit list
        def side_effect(url, *args, **kwargs):
            if "commits" in url:
                mock_response = MagicMock()
                mock_response.status_code = 200
                mock_response.json.return_value = [{"sha": "abc123"}]
                return mock_response
            else:
                return mock_get.return_value

        mock_get.side_effect = side_effect

        result = get_user_repos_and_commits("anyuser")
        # Each mocked repo has one commit
        expected = [
            "Repo: mocked_repo_1 Number of commits: 1",
            "Repo: mocked_repo_2 Number of commits: 1"
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
