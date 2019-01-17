# questioner
[![Coverage Status](https://coveralls.io/repos/github/nyambaka/questioner/badge.svg?branch=develop)](https://coveralls.io/github/nyambaka/questioner?branch=develop)
[![Build Status](https://travis-ci.org/nyambaka/questioner.svg?branch=develop)](https://travis-ci.org/nyambaka/questioner)
[![Test Coverage](https://api.codeclimate.com/v1/badges/7417fdee66c73d1eb7ae/test_coverage)](https://codeclimate.com/github/nyambaka/questioner/test_coverage)

#Introduction
Questioner is an api server that use json format to communicate.The questoner
is a meetup organizing api that allow group leader to create a meetup and add  users ,who can post questions  vote
for them as they bubble up to help to prioritize them.
users added to a meetup can post RSVP to confirm their availability for meetups and also comment on questions 
posted by their colleges

#Features

    A user can create an account
    A user can sign in 
    An administator can create meetup record
    A user can post a question
    A user can respond to meetup request (RSVP)
    User can upvote or downvote a question
    A admin can fetch all meetups 
    A user and can fetch a specific meeetup 

#Install python on your computer

    Clone the repository from github and change directory to Questioner

   $ https://github.com/nyambaka/questioner.git
   $ cd questioner

    Install a virtual environment and activate it


 $ virtualenv env
 $ source env/bin/activate

    Install all the requirements using requirements.txt

    $ pip install -r requirements.txt 

    Start the flask application

   $ export FLASK_DEBUG=1
   $ export FLASK_ENV=development
   $ export FLASK_APP=run.py
   $ flask run
   
_End points_
  
|Method 	  |Endpoint 	                     |functionality  
|-----------|--------------------------------|-------------------
|POST 	    |/api/v1/signup   	   |Create a user account
|POST 	    |/api/v1/login	   |login a user
|POST 	      |/api/v1/meetups 	   |create a meetup record.
|GET 	    |/api/v1/meetups  |	fetch all  meetups.
|GET 	    |/api/v1/meetups/<meetup_id>  |	fetch a specifc meetup.
|POST	  |/api/v1/question  |	post a question
|PATCH	  |/api/v1/question/<questin_id>/downvote  |	downvote a question
|PATCH   	|/api/v1/question/<question_id>/upvote 	 |downvote a question
|POST|/api/v1/meetups/<meetup_id>/rsvp|post an rsvp
  
  
 #sample data
| route  | sample data
|--------|---------------
|/api/v1/signup |{"firstname":"nelson","lastname":"nyambaka","othername":"nyambaka","email":"nelsonnyamgbaka@gmail.com","phonenumber":"0700741837","username":"nelfly","registered":"2018-01-20","isadmin":1,"password":"nelsonking"}
|/api/v1/login |{"email":"nelsonnyamgbaka@gmail.com","password":"nelsonking"}   or {"username":"nelfly","password":"nelsonking"}
|/ api/v1/question|{"userid":1,"body":"javascript is the best language i think we should not discuss this","meetup":4}
|/api/v1/meetups/<meetup_id>/rsvp|{"rsvp":"yes","userid":1,"meetup":4}
|/api/v1/meetups |{"user":[1,2,3],"on":"Jun 1 2045","topic":"javascript is best languange please lets not discuss","location":"mau summit"}
#author
Nelson Nyambaka