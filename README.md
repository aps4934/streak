# GitHub Daily Commit Bot

This bot automates daily commits to a GitHub repository to help maintain your daily contribution streak.

## Prerequisites

- Python 3.6+
- Git installed on your system
- A GitHub account
- A public GitHub repository (private repos don't count towards streaks)

## Setup

### 1. Create a GitHub Personal Access Token

1. Go to [GitHub Settings > Developer settings > Personal access tokens](https://github.com/settings/tokens).
2. Click "Generate new token (classic)".
3. Give it a name like "Daily Commit Bot".
4. Select scopes: `repo` (full control of private repositories) or `public_repo` if only using public repos.
5. Copy the token (keep it secure!).

### 2. Create or Use a Repository

- Create a new public repository on GitHub (e.g., `daily-streak`).
- Clone it to your local machine: `git clone https://github.com/yourusername/repo-name.git`

### 3. Set Up Environment Variables

1. Copy `.env.example` to `.env`.
2. Fill in your details:
   ```
   GITHUB_TOKEN=your_token_here
   GITHUB_USERNAME=your_username
   REPO_NAME=your_repo_name
   LOCAL_REPO_PATH=C:/path/to/your/cloned/repo
   ```
   - Use absolute paths for `LOCAL_REPO_PATH`.
   - Ensure the path uses forward slashes or escaped backslashes.

### 4. Install Dependencies

Run:
```
pip install -r requirements.txt
```

### 5. Test the Script

Run the script manually:
```
python main.py
```
It should make 6-8 commits if none exist for today.

### 6. Schedule Execution on Internet Connection (Windows Task Scheduler)

1. Open Task Scheduler (search for it in Start menu).
2. Click "Create Task" (not Basic Task).
3. Name: "Daily GitHub Commit on Network Connect"
4. In Triggers tab, click "New".
5. Begin the task: "On an event"
6. Log: Microsoft-Windows-NetworkProfile/Operational
7. Source: NetworkProfile
8. Event ID: 10000 (network connected)
9. Click OK.
10. In Actions tab, click "New".
11. Action: Start a program.
12. Program/script: `run.bat` (or full path to run.bat)
13. Start in: The directory containing run.bat (e.g., `D:\Github Bot`)
14. Click OK.
15. In Conditions tab, check "Start only if the following network connection is available" and select "Any connection".
16. Finish and test by disconnecting/reconnecting to network.

## How It Works

- Checks the latest commit date in the repository.
- If no commit today, makes 6-8 commits by appending timestamps to `streak.txt` and pushing each one.
- Uses your GitHub token for authentication.
- Runs automatically whenever your system connects to the internet on a given day.

## Security Notes

- Never commit the `.env` file (add it to `.gitignore`).
- Keep your token private.
- The repository should be public for contributions to count towards your streak.

## Troubleshooting

- Ensure all environment variables are set correctly.
- Check that the local repo path is correct and the repo is initialized.
- Verify Git is installed and configured.
- If push fails, check token permissions and repository access.
- If the task doesn't trigger, check Event Viewer for the network event ID.
