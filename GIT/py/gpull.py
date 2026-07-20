import sys
from utils import run_git

if len(sys.argv) < 2:
    print("Usage: gpl <branch>")
else:
    branch = sys.argv[1]
    run_git(["git", "pull", "origin", branch])