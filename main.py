import os
from dotenv import load_dotenv
from git import Repo
from datetime import datetime

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')
LOCAL_REPO_PATH = os.getenv('LOCAL_REPO_PATH')

if not all([GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME, LOCAL_REPO_PATH]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

# Initialize the repository
repo = Repo(LOCAL_REPO_PATH)

import random

# Check if there are any commits
today = datetime.now().date()
if repo.head.is_valid():
    latest_commit = repo.head.commit
    commit_date = datetime.fromtimestamp(latest_commit.committed_date).date()
    if commit_date == today:
        print("Already committed today. Skipping.")
        exit(0)
else:
    print("No commits yet. Proceeding with first commit.")

# Number of commits: random between 6 and 8
num_commits = random.randint(6, 8)
print(f"Making {num_commits} commits today.")

# Update remote URL with token for authentication
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
origin = repo.remote('origin')
origin.set_url(remote_url)

streak_file_path = os.path.join(LOCAL_REPO_PATH, 'streak.txt')

for i in range(num_commits):
    # Update the streak file with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(streak_file_path, 'a') as f:
        f.write(f"{timestamp} - Commit {i+1}\n")

    # Add, commit
    repo.index.add(['streak.txt'])
    repo.index.commit(f"Daily commit {i+1}: {timestamp}")

    # Push after each commit
    origin.push()

print(f"{num_commits} commits completed successfully.")
