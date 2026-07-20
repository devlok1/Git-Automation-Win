*****GIT Automation Cli*****

A simple automation of git commands using python & Windows Batch scripts for learning automation.

*****Requirements*****

Python 3.10+
Git installed
Windows Command Prompt or PowerShell

*****Installation*****

Clone the repository.
git clone <repository-url>
Update each .bat file so it points to the correct location of the corresponding Python script.

Example:

@echo off
python C:\Path\To\Git\py\ga.py %*
Add the folder containing the .bat files to your Windows PATH.
Open a new terminal.

NOTE: 
python "%~dp0..\GIT\py\ga.py" %*  // example of ga(git add)
This command is used in the bat files , make sure to add the bin folder in your PAth of environmental variables.
Otherwise it won't run.

***Usage***

Make sure to first create a Repo first. 
Add the bin file to PATH of Environment variables.

Initialize a repository: gi
Check status: gs
Stage all changes: ga
Commit changes: gc Comment-Here
Added Git automation utilities

Create a branch: gb
feature-login

View remotes: gr 
//output should be https://github.com/your_username/repo_name.git(fetch & pull each)

Pull from a branch:  gpull main

Push commits:  gpsh

***Future Improvements***

Command-line argument parsing with argparse
Colored terminal output
Automatic upstream branch detection
Checkout and branch switching commands
Merge and rebase helpers
Git log shortcuts
Better error handling
Cross-platform support (Windows/Linux)
Learning Goals


This project was built to:

Practice Python scripting
Learn process automation with subprocess
Understand Git workflows
Build reusable command-line utilities
Improve software engineering and automation skills
