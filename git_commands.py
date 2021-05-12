#in the name of Allah the most merceful
#in the terminal
git clone <git url>
# download the reprository from git-hub to my local machine
#in the terminal cd to the reprository

git add <filename>
#add a file to the reprosiotory

git commit -m "message"
#save a snapshot of the changes I made to my file

git push
# saving the changes online

git commit -am "Message"
#commiting and adding all files

git pull
#getting the latest version of the file from github

#fixing merge conflicts
#open file and delete the unwanted lines of code

git log
# get hitstory of all changes

git reset --hard <commit>
#reset the code to specific commit

git reset --hard origin/master
#reset the code the origin ,state take care

####################branching######################
git branch
#tell you which branch you are if __name__ == '__main__':

git checkout -b <branch name>
#create and change head to the new branch

git checkout <branchname>
#change your current branch to branchname

git merge <branchname>
#merge the branchname to the current branching

fork
# from the github site - you take a copy from the github repository , used in opensource and large projects
#after you are done with writing code

pull request
#you submit a request pull to be allowed to get your code  accepted in the repository


##############github pages########
1-make new repository url.github.io
2-write your code
3- open git hub settings
4- github pages
5-click on your url
then your site is now any one can access it online
