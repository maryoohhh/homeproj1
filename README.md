# homeproj1

## Adding collaborators
1. Settings
2. Manage Access
3. Invite a collaborator
4. Search using username, full name, or email and select
5. Add

## Opening vscode on terminal
`code .`

## Creating and opening directory
1. `mkdir [directory_name]`    
2. `cd [directory_name]`

## Cloning and opening repos
1. `git clone [repo_address]`
2. `cd [repo_name]`

## Adding branch
1. `git checkout -b [branch_name]`

**Best practice: Why you should never push to branch *main***
* *main* branch, formally known as *master* should be stable.
* *main* branch is considered as "production" or "live". Any changes pushed directly can break the application.
* Industry practice, *main* branch is typically a locked branch. The only way you can merge changes is through creating PR (pull request) with at least two reviewers.

## Fetching and pulling
**Fetch** - retrieves any commits, references, branches, and files from a remote repository

**Prune** - cleans up local references to remote branch and prunes all deleted remote branch

**Pull** - used to fetch and download content from a remote repository and immediately update local repository to match that content

1. `git fetch --prune --all`    
2. `git pull`

## Adding, commiting, and pushing
**Best practice:** always do a git fetch and git pull prior to adding, commiting and pushing.

1. Save changes to local     
2. `git add '[filename]'` or `git add .` (to add all files)
3. `git commit -m 'message'`
4. `git push origin [branch_name]`

## Creating a Pull Request
1. Pull request
2. Create pull request
3. Add comments if necessary

**Best practice:** after merging your featured branch through pull request to your *main* branch, always delete the branch to avoid branching off of that featured branch that could cause merge conflicts. Always branch out of *main*.
