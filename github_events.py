import requests
from pprint import pprint
import base64
from github import Github, Auth, GithubIntegration
import os
from dotenv import load_dotenv
import json


load_dotenv()


GH_TOKEN = os.environ["GITHUB_TOKEN"]
GH_USERNAME = os.environ["GITHUB_USERNAME"]

# Authenticate w token
auth = Auth.Token(GH_TOKEN)

# Pygithub object
g = Github(auth=auth)


# Get user by username
user = g.get_user(GH_USERNAME)

for event in user.get_events():
    pprint(event.raw_data)


# for repo in user.get_repos():
#     print(repo)

# List of dicts for commits
# commits = []

# coms = repo.get_commits('main')

# Prints Commit objects w sha identifier
# for c in coms:
#     print(c)

# Access specific commit by sha or all commits w raw data loop
# commit = repo.get_commit(sha="1038bbf8a3314b1e58f517a70c458be2e6b21446")
# pprint(commit.commit.raw_data)
#
# all_commits = repo.get_commits('main')
# for commit in all_commits:
#     commit_timestamp = commit.commit.author.date
#     commit_msg = commit.commit.message
#     commit_sha = commit.commit.sha
#     commit_dict = {
#         'sha': commit_sha,
#         'timestamp': commit_timestamp,
#         'message': commit_msg
#     }
#     commits.append(commit_dict)
#
# pprint(commits)

## See all possible repo attributes
# pprint(dir(repo))

# # Access attributes in repo object
# def print_repo(repo):
#     print(f"Repo Full Name: {repo.full_name}")
#     print(f"Description: {repo.description}")
#     print(f"Date Created: {repo.created_at}")
#     print(f"Date of last push: {repo.push_at}")
#     print(f"Home Page: {repo.homepage}")
#     print(f"Number of Forks: {repo.forks}")
#     print(f"Number of Stars: {repo.stargazers_count}")
#     # repo contents
#     print("Contents:")
#     for content in repo.get_contents(""):
#         print(content)

# Create list of repos to pull via api...pull raw data once, then can pull whatever you want from it to lessen api calls
# my_repos = ['100-movies-to-watch', 'advanced-flask-blog', 'blog-with-users']

# Get user by username
# user = g.get_user(GH_USERNAME)
# repo = g.get_repo("ksg-dev/100-movies-to-watch")

# for repo in user.get_repos():
#     print(repo)



# # List of dicts for commits
# commits = []
#
# for name in my_repos:
#     repo = g.get_repo(f"{GH_USERNAME}/{name}")
#     all_commits = repo.get_commits()
#     for commit in all_commits:
#         commit_data = commit.commit.raw_data
#         commits.append(commit_data)
#
#
# with open("repos.json", "a") as file:
#     json.dump(commits, file)



