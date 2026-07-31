"""
first we create a readme file = touch README.md
git init = initialize the folder
git status = shows status of untracked and tracked files
git add filename = for adding single file
git add . = for adding multiple files to the working tree
git commit -m "messsage" = for commiting the files and also message
git log = shows commits with branches and author and date
git branch -M Main = master branch changed name to Main
git remote add origin https://github.com/iggurman/school_management.git
git remote remove origin = removes the origin
git remote -v = origin  https://github.com/iggurman/school_management.git (fetch)
                origin  https://github.com/iggurman/school_management.git (push)
git push origin main = pushes code to origin branch main
branch= a branch is an independent line of development
git switch/checkout -b feature/school = create a branch from main
now to push the changes from side branch to main branch
1) go to github and pr(pull request) = compare and pull request
2) git pull origin main then 
git push origin main
"""

"""
# Test: testing before product

# git checkout -b feature/{featurename}
# git status
# git add file/name, git add .
# git commit -m ""
# git push origin feature/{featurename}

# part-2

# git checkout staging/main
# staging/main : git pull origin staging/main

# 1. PR raise from GitHub
# 2. git merge origin/feature/{featurename}
# 3. git push origin main/staging
"""

"""
for commiting this should be followed
# type(scope):msg

git commit -m "feat(school):Add school API"

# Add school API : feat(school):Add school API
# Add school API : fix(school):Add school API
# """

"""
git log --online
git log --graph --oneline
git commit --amend
git stash
"""