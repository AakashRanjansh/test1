# subhakaarya-backend

follow these steps: 
-> Clone git repo
-> pip install -r requirements.txt
-> Create .env file and insert the following to it: 
```
SECRET_KEY = randomkey
DB_NAME = db.sqlite3
DB_USER = root
DB_PASSWORD = 
DB_HOST = localhost
```

->
```
python manage.py migrate --run-syncdb
```
->
```
python manage.py runserver
```
