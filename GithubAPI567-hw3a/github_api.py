# Tamara Gonzalez Ibarra
# SSW 567 - Fall 2025

import requests

"""
This function returns a list of tuples given a Github user ID: (repo_name, number_of_commits)
"""
def get_repos_and_commits(user_id):
    
    repos_url = f"https://api.github.com/users/{user_id}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code != 200:
        raise Exception(f"Error fetching repos for user {user_id}: {repos_response.status_code}")

    repos_data = repos_response.json()
    results = []

    for repo in repos_data:
        repo_name = repo.get("name")
        commits_url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
        commits_response = requests.get(commits_url)

        if commits_response.status_code != 200:
            num_commits = 0  # Default to 0 if we can’t fetch commits
        else:
            commits_data = commits_response.json()
            num_commits = len(commits_data)

        results.append((repo_name, num_commits))

    return results


# Tests the function by running it directly with my own Github user.
if __name__ == "__main__":
    user = "emo-cheesecake"
    repos_and_commits = get_repos_and_commits(user)
    for repo, commits in repos_and_commits:
        print(f"Repo: {repo} Number of commits: {commits}")
