> If you accidentally mistype a commit message, you can change it using the --amend flag:

    - git commit --amend - m "new message"

> To compare the state of your files with those in the staging area

    - git diff -r HEAD

> To compare the state of a specific file with the same in the staging area
    
    - git diff -r HEAD filename

> Get the logs of a specifc file 
    - git log filename

> Write a commit with a log message

    - git commit (without -m "message", this will open a file with a test editor)