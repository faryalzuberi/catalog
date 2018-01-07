# Catalog
This project consists of a item catalog website that includes Create, Read, Update and Delete operations for users that are logged in via gmail. The website is served by a Python3 script that queries from a SQLalchemy database at the backend.
# Pre-requisties
This project requires Python3, SqlAlchemy and a Virtual Machine set up and configured with vagrant. 
# Installation
Download the project file and extract it into the shared vagrant directory and from the command line change directories to the /catalog file. 
Populate the database by running the command
```
python3 populatedb.py
```
Run the server using 
```
python3 final_project.py
```
Open the catalog website from your preferred browser at [Home](http://localhost:5000/catalog)
To perform CRUD operations login with your gmail credentials at [Login](http://localhost:5000/login)
