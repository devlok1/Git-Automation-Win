import subprocess
from sys import stderr 

def git_init():
      try:
            subprocess.run(["git", "init"], check = True, capture_output=True, text=True)
            print("git initialized successfully." )
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while initializing git: {e.stderr}")

def git_status():
      try:
            result = subprocess.run(["git", "status"], check = True, capture_output=True, text=True)
            print("git status executed successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while checking git status: {e.stderr}")



def git_add():
      try:
            result = subprocess.run(["git", "add", "."], check = True, capture_output=True, text=True)
            print("git added successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while adding to git: {e.stderr}")



def git_commit():
      try:
            commit_message = input("Enter commit message: ")
            result = subprocess.run(["git", "commit", "-m", commit_message], check = True, capture_output=True, text=True)
            print("git committed successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while committing to git: {e.stderr}")



def git_branch(branch_name):
      try:
            result = subprocess.run(["git", "branch", branch_name], check = True, capture_output=True, text=True)
            print(f"git branch '{branch_name}' created successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while creating git branch: {e.stderr}")



def git_push():
      try:
            result = subprocess.run(["git", "push"], check = True, capture_output=True, text=True)
            print("git pushed successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while pushing to git: {e.stderr}")
            
            

def git_pull(repo_url=None):
      try:
            result = subprocess.run(["git", "pull"], check = True, capture_output=True, text=True)
            print("git pulled successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while pulling from git: {e.stderr}")



def git_clone(repo_url):
      try:
            result = subprocess.run(["git", "clone", repo_url], check = True, capture_output=True, text=True)
            print("git cloned successfully.")
            print(result.stdout)
      except subprocess.CalledProcessError as e:
            print(f"Error occurred while cloning git repository: {e.stderr}")



if __name__ == "__main__":
      git_init()
      git_status()
      git_add()
      git_commit()
      git_branch(input("Enter the name of the new branch: "))
      git_clone(input("Enter the repository URL to clone: "))
      git_push()
      git_pull()
      git_clone(input("Enter the repository URL to clone: "))