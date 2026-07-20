import sys
from utils import run_git

if len(sys.argv) == 1:
    run_git(["git", "push"])
elif len(sys.argv) == 2:
    run_git(["git", "push", "-u", "origin", sys.argv[1]])
else:
    print("Usage: gpsh [branch]")