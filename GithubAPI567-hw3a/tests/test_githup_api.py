# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import unittest
from github_api import get_repos_and_commits

class TestGitHubAPI(unittest.TestCase):

    def test_valid_user(self):
        # Tests with a given GitHub user
        result = get_repos_and_commits("richkempinski")
        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) for item in result))

        #Tests with my personal Github
        result1 = get_repos_and_commits("emo-cheesecake")
        self.assertIsInstance(result1, list)
        self.assertTrue(all(isinstance(item, tuple) for item in result))

    def test_invalid_user(self):
        with self.assertRaises(Exception):
            get_repos_and_commits("thisuserdoesnotexist123456")

    def test_repo_and_commit_structure(self):
        result = get_repos_and_commits("richkempinski")
        if result:  # If there are repos
            repo_name, commits = result[0]
            self.assertIsInstance(repo_name, str)
            self.assertIsInstance(commits, int)

if __name__ == "__main__":
    unittest.main()