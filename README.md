### Project Name
# Photomoto
#### Author
### Kahiga Ndegwa

## Description
This web app app allows you to 
log in, log out, comment,like, add a photo,sign out.

## Live Link (feel free to experiment all features)
[View Site](https://photomoto.herokuapp.com/)


## Setup Instructions:
### Requirements

##### 1. Clone the repository
Clone the the repository by running 

   ```bash
   git clone https://github.com/kahiga2244/Django-photoMot.git
   ```
 or download a zip file of the project from github
 

Navigate to the project directory
```bash
cd django-1
```

##### 2. Create a virtual environment
 Install `Virtualenv` 

   ```prettier
   pip install virtualenv
   ```

To create a virtual environment named `virtual`, run

   ```prettier
   virtualenv virtual
   ```
To activate the virtual environment we just created, run

   ```bash
   source virtual/bin/activate
   ```

##### 3. Create a database or you can use sqlite provided by django framework
You'll need to create a new postgress database, Type the following command to access postgress
   ```bash
    $ psql
   ```
   Then run the following query to create a new database named ```your db``` 
   ```prettier
   $ CREATE DATABASE your db
   ```


#####  4.Install dependencies
To install the requirements from `requirements.txt` file,

   ```prettier
   pip install -r requirements.txt
   ```

#####  5.Create Database migrations
Making migrations on postgres using django

```prettier
python3 manage.py makemigrations 
```

 
then run the command below;

 ```bash
 python3 manage.py migrate
 ```

##### 6.Run the app
To run the application on your development machine, 

    python3 manage.py runserver

### Running Tests
>To run tests;

    python3 manage.py test

## Technologies Used
* Django
* Python
* Html
* Css
* Javascript
* Bootstrap


## User stories
>As a user of the application I should be able to:

- [X] log in and out
- [X] add pictures
- [X] like other peoples pictures
- [X] write comments 
- [X] search for other users
- [X] follow them

## Collaboration Information
* Clone the repository
* Make changes and write tests
* Push changes to github
* Create a pull request


## Bugs
There are no know bugs at the moment

## License
(http://opensource.org/licenses/MIT)
>MIT license &copy;  2021 kahiga2244
