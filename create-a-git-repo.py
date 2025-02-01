import subprocess
import sys

def create_github_repo(repo_name, private=True, description="", add_readme=True):
    """Creates a GitHub repository using the gh CLI tool."""
    
    # Determine repository visibility
    visibility = "private" if private else "public"
    
    # Construct the gh repo create command
    command = [
        "gh", "repo", "create", repo_name,
        "--{visibility}".format(visibility=visibility),
        "--description", description
    ]
    
    if add_readme:
        command.append("--enable-issues")
        command.append("--enable-wiki")
        command.append("--add-readme")
    
    try:
        # Execute the command
        subprocess.run(command, check=True)
        print(f"Successfully created repository: {repo_name}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error creating repository: {e}")
        sys.exit(1)

if __name__ == "__main__":
    repo_name = input("Enter the name of the repository: ")
    visibility = input("Should the repository be private? (yes/no): ").strip().lower() == "yes"
    description = input("Enter a description for the repository: ")
    add_readme = input("Would you like to add a README? (yes/no): ").strip().lower() == "yes"
    
    create_github_repo(repo_name, private=visibility, description=description, add_readme=add_readme)
