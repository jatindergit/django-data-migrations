# django-data-migrations
Django data migrations to merge database table fields

##Problem
Initially, users table have first_name and last_name fields. After deploying the project on 
production, we realized that not every user in the system has a last_name. This results in enough 
empty rows for last_name. Now the solution is, merge first_name and last_name fields into one field 
that is full_name. How will you do this without losing any data on production?

###BE EXTRA CAREFUL ON PRODUCTION!!!
