# Esusu

This is a REST API for a Esusu Confam ltd. built using Django REST Framework
The API is meant to do the following:
1. Enable anyone to input their basic details thereby creating an account
2. Enable a user to search for existing public groups and join them
3. Enable a user to create new groups and thereby become the admin  of the created group
4. Choose a random member of the group as receiver of contributions for the month
5. Enable an admin to edit group information including members, maximum capacity, periodic savings amount, name, description and whether or not the group is searchable
6. Enables an admin to see members of his group and how much they have saved on the group
7. Enables members to pay the specified peroidic savings amount into their groups

## Requirements
1. PC or Mac or Linux OS
2. Python (3+)
3. Pip

## Setup
Create a virtual environment to isolate our package dependencies locally
`python3 -m venv env`
`source env/bin/activate`
On Windows use `env\Scripts\activate`

Install Django and django Rest framework into the virtual environment
```
pip install django
pip install djangorestframework
```

Clone the git repo to the directory

Make and apply migrations, then run Django server from the directory
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```


## API Endpoints

|URL|Request Method|Description|Access|
|---|---|---|---|
|/members/|GET|Returns a list of members with their basic details|Anyone|
|/members/|POST|Creates new member (POST data: username,password,first_ame,last_name,email|Anyone|
|/members/pk/|GET|Returns specific member details|Logged specific member|
|/members/pk/|PUT|Updates member details||Logged in specific member|
|/members/pk/|PATCH|Partially updates member details||Logged in specific member|
|/members/pk/|DELETE|Deletes member from database||Logged in specific member|
|/groups/|GET|Displays list of public groups|Logged in members|
|/groups/|POST|Creates a new group (POST data:)|Logged in members|
  




API can also be accessed using djangorestframework's web browsable API
