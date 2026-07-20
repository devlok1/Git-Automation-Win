import subprocess

def run_git(command):
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            print(result.stdout)

        return True

    except subprocess.CalledProcessError as e:
        print(e.stderr)
        return False