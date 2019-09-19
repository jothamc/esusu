# Esusu

This is a REST API for a Esusu Confam ltd. built using Django REST Framework
The API is meant to do the following:
1. Enable anyone to input their basic details thereby creating an account
2. Enable a user to search for existing public groups and join them
3. Enable a user to create new groups and thereby become the admin  of the created group
4. Choose a random member of the group as receiver of contributions for the month
5. Enable an admin to edit group information including members, maximum capacity, periodic savings amount, name, description and whether or not the group is searchable
6. Enables an admin to see members of his group and how much they have saved on the group
7. Enables members to pay the specified periodic savings amount into their groups
8. Enable an admin to add a member to his group using the user's username
9. Enable an admin to send out an invitation URL which when accessed by a logged-in member adds the member to the group

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
|/members/pk/|PUT|Updates member details||Logged in member|
|/members/pk/|PATCH|Partially updates member details||Logged in member|
|/members/pk/|DELETE|Deletes member from database||Logged in member|
|/groups/|GET|Displays list of public groups|Logged in members|
|/groups/|POST|Creates a new group (POST data: name,description,max_capacity,savings_amount,is_searchable)|Logged in members|
|/groups/pk/|GET|Returns full details of the group|Group admin|
|/groups/pk/|PUT|Updates group details|Group admin|
|/groups/pk/|PATCH|Partially updates group details|Group admin|
|/groups/pk/|DELETE|Deletes group from database|Group admin|
|/groups/pk/payments/|GET|Returns all payments or member payment to group admin or member respectively|Group admin or logged in member|
|/groups/pk/payments/|POST|Creates a new payment into the group, automatically adding relevant member details|Logged in group member|
|/groups/pk/payments/username/|GET|Returns details of member's payment in group|Group admin or logged in member|
|/groups/pk/payments/username/|PATCH|Increments payment amount using group's saving amount (No data should be sent)|Group admin or logged in member|
|/groups/pk/payments/username/|DELETE|Deletes payment from database|Group admin or logged in member|
|/groups/pk/add-username|PATCH|Adds member to the group using member's username|Group admin|
|/groups/pk/invite-uuid/|PATCH|Add logged-in member to the group whose uuid is called|Logged-in member|




API can also be accessed using djangorestframework's web browsable API
