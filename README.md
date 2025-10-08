# GitHub Daily Commit Bot

This bot automates daily commits to a GitHub repository using GitHub Actions to help maintain your daily contribution streak.

## Prerequisites

- A GitHub account
- A public GitHub repository (private repos don't count towards streaks)
- GitHub Actions enabled on the repository (default for public repos)

## Setup

### 1. Create or Use a Repository

- Create a new public repository on GitHub (e.g., `daily-streak`).
- Upload the bot files: `streak.txt`, `.github/workflows/daily-commit.yml`, `README.md`, etc.

### 2. Enable GitHub Actions

- Go to your repository on GitHub.
- Ensure Actions are enabled (Settings > Actions > General).
- The workflow will run automatically on the schedule.

### 3. Manual Trigger (Optional)

- You can manually trigger the workflow from the Actions tab on GitHub.

## How It Works

- The GitHub Actions workflow runs daily at 10:00 AM UTC (or manually).
- Checks the latest commit date in the repository.
- If no commit today, makes 6-8 commits by appending timestamps to `streak.txt` and pushing each one.
- Uses GitHub's built-in token for authentication.
- No local setup or commands needed; runs entirely on GitHub's servers.

## Security Notes

- The repository should be public for contributions to count towards your streak.
- GitHub Actions handle authentication securely.

## Troubleshooting

- Check the Actions tab on GitHub for workflow runs and logs.
- Ensure the repository is public.
- If commits don't appear, verify the workflow file is in `.github/workflows/`.
- Workflow runs at UTC time; adjust cron if needed.
