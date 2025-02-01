import os
import subprocess
import platform

def detect_linux_distro():
    """Detects the Linux distribution."""
    try:
        distro = platform.linux_distribution()[0].lower()
    except AttributeError:
        try:
            import distro
            distro = distro.id()
        except ImportError:
            print("Please install the 'distro' package using: pip install distro")
            return None
    
    return distro

def install_git_and_gh(distro):
    """Installs Git and GitHub CLI based on the detected Linux distribution."""
    if not distro:
        print("Could not detect Linux distribution.")
        return

    if "ubuntu" in distro or "debian" in distro:
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "-y", "git", "gh"], check=True)
    elif "fedora" in distro or "centos" in distro or "rhel" in distro:
        subprocess.run(["sudo", "dnf", "install", "-y", "git", "gh"], check=True)
    elif "arch" in distro or "manjaro" in distro:
        subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"], check=True)
        subprocess.run(["sudo", "pacman", "-S", "git", "github-cli", "--noconfirm"], check=True)
    else:
        print(f"Unsupported Linux distribution: {distro}")
        return

    print("Git and GitHub CLI have been installed successfully.")

if __name__ == "__main__":
    distro = detect_linux_distro()
    print(f"Detected Linux distribution: {distro}")
    install_git_and_gh(distro)

