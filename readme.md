person-finder-server
The backend server and image processor for my academic project kodona which is an application to find missing peson.

To get started:
install dependencies
pip3 install -r requirments.txt
install postgres database
create a database named kodona_db
create a user named kodona_user password as password
create the database tables
python3 manage.py migrate
run the server
python3 manage.py runserver
hit the server at localhost:8000/
