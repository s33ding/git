import subprocess

def list_github_repos():
    """Lists all repositories associated with the authenticated GitHub account."""
    try:
        print("Fetching GitHub repositories...")
        subprocess.run(["gh", "repo", "list"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error listing repositories: {e}")
        
if __name__ == "__main__":
    list_github_repos()

