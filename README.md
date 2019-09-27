# One stop location
An initiative....

## Installation
To install Django on your local machines use the below link
1.[Django Installation](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)

2. Install MYSQL
 Since the entire database is based on mysql format ,create a mysql server on your machine . To install mysql use the below link:
 [mysql](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
 
PLEASE NOTE ..
After creating database as the above step follow the below commands
 
 3.Creating the database
 Login into your mysql user account using command $mysql -u 'user name' -p
 In mysql shell create a database using command 
 
 ```bash
 mysql> CREATE DATABASAE 'db name';
 ```
 4.Configure database for adding tables
 In the terminal shell write the command 
 ```bash


 $sudo nano /etc/mysql/.my.cnf
 ```
 It will open a empty file write out user credentials there
 ```bash
 
 [client]
 database='db_name'    
 user='user name'
 password='password'
 default-character-set=utf8
 ```
 !Note: write all the credentials without ' '
 
 5.Restart your mysql server:
 Enter the following commands to restart the server
 ```bash
 $ systemctl daemon-reload
 $ systemctl restart mysql
 ```
 if everything is configured well , your database will be configured with the app
 
 6.To add migrations to django app
 In interact directory write the following commands
 ```bash
 ~/interact$ python3 manage.py makemigrations
 ~/interact$ python3 manage.py migrate
 ```
 7.Finally running your machine:
 ```bash
 ~/interact$ python3 manage.py runserver
 ```
 Your server will start at http://127.0.0.1:8000/interact/
 
 ## Congrates you just started interact on your local server
 Keep contributing . Hav a bug free code :)
 
 
 
 

