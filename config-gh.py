import subprocess

def configure_gh():
    """Configures GitHub CLI (gh) by prompting user to log in and setting default configurations."""
    try:
        # Authenticate with GitHub
        print("Authenticating GitHub CLI...")
        subprocess.run(["gh", "auth", "login"], check=True)

        # Grant full control permissions
        print("Granting full control permissions...")
        subprocess.run(["gh", "auth", "refresh", "-h", "github.com", "-s", "delete_repo"], check=True)
        subprocess.run(["gh", "auth", "refresh", "-h", "github.com", "-s", "repo"], check=True)
        subprocess.run(["gh", "auth", "refresh", "-h", "github.com", "-s", "admin:repo_hook"], check=True)
        
        # Set default GitHub username
        username = input("Enter your GitHub username: ")
        subprocess.run(["gh", "config", "set", "user", username], check=True)

        # Set default editor (optional)
        editor = input("Enter your preferred text editor (e.g., vim, nano, code): ")
        if editor:
            subprocess.run(["gh", "config", "set", "editor", editor], check=True)

        # Set default GitHub protocol (https or ssh)
        protocol = input("Enter preferred Git protocol (https/ssh): ").strip().lower()
        if protocol in ["https", "ssh"]:
            subprocess.run(["gh", "config", "set", "git_protocol", protocol], check=True)
        else:
            print("Invalid protocol. Defaulting to https.")
            subprocess.run(["gh", "config", "set", "git_protocol", "https"], check=True)

        print("GitHub CLI has been configured successfully with full control permissions!")
    except subprocess.CalledProcessError as e:
        print(f"Error configuring GitHub CLI: {e}")

if __name__ == "__main__":
    configure_gh()

