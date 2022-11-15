# Studying git

In this repository I show some Git commands that I learned when I was studying.

![Git Logo](https://t.ctcdn.com.br/JyYOtyrVhIK_AagtBY2lKWT4otg=/135x0:1858x971/512x288/smart/filters:format(webp)/i329956.jpeg)



> Use Git commands to help keep track of changes made to a project:

- git init - creates a new Git repository
- git status - inspects the contents of the working directory and staging area
- git add - adds files from the working directory to the staging area
- git diff - shows the difference between the working directory and the staging area
- git commit - permanently stores file changes from the staging area in the repository
- git log - shows a list of all previous commits



 > If you accidentally mistype a commit message, you can change it using the --amend flag:

- git commit --amend - m "new message"

> To compare the state of your files with those in the staging area

- git diff -r HEAD

> To compare the state of a specific file with the same in the staging area

- git diff -r HEAD filename

> Get the logs of a specifc file:
 
- git log filename

> Write a commit with a log message

- git commit (without -m "message", this will open a file with a test editor)

> Discards changes in the working directory.

- git checkout HEAD filename: 

> Unstages file changes in the staging area:

- git reset HEAD filename. 

> Resets to a previous commit in your commit history: 

- git reset commit_SHA.

> You also can add multiple files to the staging area with a single command:

- git add filename_1 filename_2

[Git Extension for VS Code](https://marketplace.visualstudio.com/items?itemName=GitExtensionsApp.v341)

