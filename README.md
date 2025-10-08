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
It should make a commit if none exists for today.

### 6. Schedule Daily Execution (Windows Task Scheduler)

1. Open Task Scheduler (search for it in Start menu).
2. Click "Create Basic Task".
3. Name: "Daily GitHub Commit"
4. Trigger: Daily, set time (e.g., 10:00 AM).
5. Action: Start a program.
6. Program/script: `python` (or full path to python.exe)
7. Add arguments: `main.py`
8. Start in: The directory containing main.py (e.g., `D:\Github Bot`)
9. Finish and test by running the task manually.

## How It Works

- Checks the latest commit date in the repository.
- If no commit today, makes 6-8 commits by appending timestamps to `streak.txt` and pushing each one.
- Uses your GitHub token for authentication.

## Security Notes

- Never commit the `.env` file (add it to `.gitignore`).
- Keep your token private.
- The repository should be public for contributions to count towards your streak.

## Troubleshooting

- Ensure all environment variables are set correctly.
- Check that the local repo path is correct and the repo is initialized.
- Verify Git is installed and configured.
- If push fails, check token permissions and repository access.
