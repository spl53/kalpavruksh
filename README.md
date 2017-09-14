# kalpavruksh
short project
################################
- install rest framwork
	sudo pip install djangorestframework
- install mysql-client and mysql server
- run python manage.py makemigrations
- run python manage.py migrate
- run 'django-admin loaddata default_data.txt' to load the data in database
	or load 'quizdb.sql' dump data in mysql  using mysqldump command

- use apikey from mysql tanent table  for every request other wise request will not get complete
- pass apikey in get request for ex.
  - http://127.0.0.1:8000/get_question/?api_key=dfe4ter3df
- get mathed question only  by  adding additional parameter in request as query
  - http://127.0.0.1:8000/get_question/?api_key=dfe4ter3df&query=Name
