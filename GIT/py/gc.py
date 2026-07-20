import sys
from utils import run_git

if len(sys.argv) < 2:
    print("Usage: gc <commit message>")
else:
    message = " ".join(sys.argv[1:])
    run_git(["git", "commit", "-m", message])