# Studying git

In this repository I show some Git commands that I have learned.

![Git Logo](https://t.ctcdn.com.br/JyYOtyrVhIK_AagtBY2lKWT4otg=/135x0:1858x971/512x288/smart/filters:format(webp)/i329956.jpeg)

> Main Git commands:

- git init - creates a new Git repository
- git status - inspects the contents of the working directory and staging area
- git add - adds files from the working directory to the staging area
- git diff - shows the difference between the working directory and the staging area
- git commit - permanently stores file changes from the staging area in the repository
- git log - shows a list of all previous commits

[Git Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=GitExtensionsApp.v341)

# Git Cheat Sheet - Quick Reference for Common Commands

## Checking Git Version
```bash
git --version
```

## Initialize a New Git Repository
```bash
git init
```

## Checking Repository Status
```bash
git status
```

## Adding Files to Staging Area
```bash
git add filename
git add .  # Adds all modified files
```

## Committing Changes
```bash
git commit -m 'Commit message'
```

## Viewing Commit History
```bash
git log
git log -3  # Show last 3 commits
git log --since='Apr 2 2024' --until='Apr 11 2024'  # Filter by date range
```

## Viewing a Specific Commit
```bash
git show <commit_hash>
```

## Comparing Changes
```bash
git diff  # Show unstaged changes
git diff --staged  # Show staged changes
git diff HEAD~1 HEAD  # Compare last two commits
```

## Reverting and Restoring Files
```bash
git revert HEAD  # Revert the last commit
git revert HEAD --no-edit  # Revert without opening an editor
git checkout HEAD~1 -- filename  # Restore a file from the previous commit
git restore --staged filename  # Unstage a file
git restore --staged  # Unstage all files
```

## Resetting to a Previous Commit
```bash
git reset <commit_hash>  # Soft reset to a previous commit
git reset --hard <commit_hash>  # Hard reset (erases changes)
```

## Working with Branches
```bash
git branch  # List branches
git checkout -b new-branch  # Create and switch to a new branch
git checkout main  # Switch back to main branch
```

## Merging Branches
```bash
git merge branch-name  # Merge a branch into the current branch
```

## Pushing Changes to Remote Repository
```bash
git remote add origin <repo_url>
git push -u origin main
```

## Pulling Latest Changes from Remote
```bash
git pull origin main
```

## Cloning a Repository
```bash
git clone <repo_url>
```

### End of Cheat Sheet
