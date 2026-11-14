import os
import sys
import random
import subprocess
from datetime import datetime, timezone, timedelta

# Default bounds: 20 to 40 commits
MIN_COMMITS = int(os.getenv("MIN_COMMITS", "20"))
MAX_COMMITS = int(os.getenv("MAX_COMMITS", "40"))

COMMITTER_NAME = "Aditya Pratap Singh"
COMMITTER_EMAIL = "aps4934@users.noreply.github.com"
TIMEZONE_OFFSET = "+0530"
IST = timezone(timedelta(hours=5, minutes=30))

script_dir = os.path.dirname(os.path.abspath(__file__))
streak_file = os.path.join(script_dir, "streak.txt")

def run():
    num_commits = random.randint(MIN_COMMITS, MAX_COMMITS)
    now_ist = datetime.now(IST)
    today_str = now_ist.strftime("%Y-%m-%d")
    
    print(f"[{today_str}] Generating {num_commits} streak commits...")
    
    is_dry_run = "--dry-run" in sys.argv
    if is_dry_run:
        print(f"[DRY RUN] Would generate {num_commits} commits for {today_str}. Exiting.")
        return

    # Base time starts earlier in the day if running now
    base_time = now_ist - timedelta(minutes=num_commits * 2)
    
    for i in range(num_commits):
        commit_dt = base_time + timedelta(minutes=i * 2)
        iso_str = commit_dt.strftime("%Y-%m-%d %H:%M:%S %z")
        ts_display = commit_dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # Append entry to streak.txt
        with open(streak_file, "a", encoding="utf-8") as f:
            f.write(f"{ts_display} - Auto Streak #{i+1} of {num_commits}\n")
            
        subprocess.run(["git", "add", "streak.txt"], cwd=script_dir, check=True)
        
        env = {
            **os.environ,
            "GIT_AUTHOR_NAME": COMMITTER_NAME,
            "GIT_AUTHOR_EMAIL": COMMITTER_EMAIL,
            "GIT_AUTHOR_DATE": iso_str,
            "GIT_COMMITTER_NAME": COMMITTER_NAME,
            "GIT_COMMITTER_EMAIL": COMMITTER_EMAIL,
            "GIT_COMMITTER_DATE": iso_str,
        }
        
        msg = f"Automated daily commit {i+1}/{num_commits}: {ts_display}"
        subprocess.run(["git", "commit", "-m", msg], cwd=script_dir, env=env, check=True)
        
    print(f"Successfully generated {num_commits} commits.")
    
    # Push to origin
    if "--no-push" not in sys.argv:
        print("Pushing to origin...")
        subprocess.run(["git", "push", "origin", "HEAD:master"], cwd=script_dir, check=True)
        print("Push successful!")

if __name__ == "__main__":
    run()
