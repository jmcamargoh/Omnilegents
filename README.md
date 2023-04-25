# Omnilegents

## Libraries
- Python equal or superior to 3.6 version.  
- Pip tool.  
- Django framework. Automatically brings the necessary libraries for the server execution.  
- Git tool. Import and export from a GitHub repository.
- Python pandas

## Commands
The following commands are expected to be used on system cmd while located in the folder designated for the project (for Windows). Words that are in bold indicate that their name can be modified by the contributor:

### Python:
- python -m django startproject **name_of_project** (create a folder with the project)
- cd **name_of_project** (locate on the created folder)
- python manage.py runserver (to execute the local server)
- python manage.py startapp **name_of_app** (creation of the app) **IMPORTANT:** This must be done from the outside folder (not the one created with the first command of this list)
- python manage.py createsuperuser (create a user to access the admin)  

The follwing two commands must be executed after make any changes in "models.py". Every migration is going to be saved in folder "migrations":
- python manage.py migrate
- python manage.py makemigrations

### Git Commands:
- git init (to initialize the folder as a git repository)
- git add . (to add all the changes done since last commit)
- git status (to verify if all changes were detected and added)
- git commit -m "**name_of_commit**" (create the commit to push in online repository)
- git remote add origin **link_of_the_repo_to_update** (to create the link between the local repository and the one in the cloud)
- git branch -m **name_of_the_branch** (the branch that will receive the local push)
- git push -u origin **name_of_the_branch** (make te push to the designed branch)
- git clone **link_of_repo_to_clone** (clone the project from an existing repository)
