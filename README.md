# GraphQL API in Django with graphene-django


Follow the steps below to run this project:

1.  Make sure you have the following development environment:
    1.  Python 3.9.7 (You can be flexible with the version but, I have tested with this version only).
    1.  Any IDE or text editor of your choice.
    1.  Access to Command-Line or Terminal 

1.  Clone this repository.
1.  Open the terminal or command line.
1.  Navigate to the location where you cloned this repository.
1.  Install the dependencies by typing following command:
  
      `pip install -r requirements.txt`

1.  Migrate Django models to the database (SQLite) by typing following commands in order:

      `python manage.py makemigrations`
      `python manage.py migrate`
      
1.  Run the Django server by entering following commands in order:

      `python manage.py runserver`
      
Now, the project should be up and running. By default django server runs in <b>localhost:8000</b> and you should be able to access the GraphiQL interface by typing
http://localhost:8000/graphql address in the address bar of the browser.

### How to enable CORS:

To connect with this API locally, you might need to disable cors. Follow these steps mentioned in https://www.stackhawk.com/blog/django-cors-guide/ for this purpose:
