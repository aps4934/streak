import os
from dotenv import load_dotenv
from git import Repo
from datetime import datetime, timedelta
import random
import socket

# Load environment variables
load_dotenv()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')
REPO_NAME = os.getenv('REPO_NAME')
LOCAL_REPO_PATH = os.getenv('LOCAL_REPO_PATH')

if not all([GITHUB_TOKEN, GITHUB_USERNAME, REPO_NAME, LOCAL_REPO_PATH]):
    raise ValueError("Missing required environment variables. Please check your .env file.")

# Check internet connection
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        pass
    return False

if not is_connected():
    print("No internet connection. Exiting.")
    exit(0)

# Initialize the repository
repo = Repo(LOCAL_REPO_PATH)

# Update remote URL with token for authentication
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USERNAME}/{REPO_NAME}.git"
origin = repo.remote('origin')
origin.set_url(remote_url)

streak_file_path = os.path.join(LOCAL_REPO_PATH, 'streak.txt')

# Start date: 2024-01-01
start_date = datetime(2024, 1, 1)
# End date: 2024-01-31
end_date = datetime(2024, 1, 31)

current_date = start_date
while current_date <= end_date:
    # Number of commits: random between 2 and 3
    num_commits = random.randint(2, 3)
    print(f"Making {num_commits} commits for {current_date.date()}.")

    for i in range(num_commits):
        # Set environment variables for date
        date_str = current_date.strftime("%Y-%m-%dT%H:%M:%S+0530")
        os.environ['GIT_AUTHOR_DATE'] = date_str
        os.environ['GIT_COMMITTER_DATE'] = date_str

        # Update the streak file with timestamp
        timestamp = current_date.strftime("%Y-%m-%d %H:%M:%S")
        with open(streak_file_path, 'a') as f:
            f.write(f"{timestamp} - Commit {i+1}\n")

        # Add, commit
        repo.index.add(['streak.txt'])
        repo.index.commit(f"Daily commit {i+1}: {timestamp}")

    # Push after all commits for the day
    origin.push()

    # Move to next day
    current_date += timedelta(days=1)

print("Backdating completed successfully.")
