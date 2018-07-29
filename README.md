# Starting the application
### via docker-compose
```sh
$ echo "SQLALCHEMY_DATABASE_URI = \"postgresql://postgres:passwd@bambu_db_1/bambu\"" > settings.py
$ echo "SQLALCHEMY_DATABASE_URI_TEST = \"postgresql://postgres:passwd@bambu_db_2/bambutest\"" >> settings.py
$ docker-compose up --build # docker-compose version 1.20.1, build 5d8c71b was tested
```

### via python virtual environment
```sh
$ # use virtualenv version 16.0.0 at least
$ virtualenv ~/.minmedvenv
$ source ~/.minmedvenv/bin/activate

# on the application directory
$ pip install -r requirements.txt
# create settings.py with JDBC URLs to postgres database (settings.py.example given as example) 
$ python manage.py runserver
```

# Swagger docs
On http://localhost:5000/spec (not complete)

# Testing the application
```sh
$ curl -s -X POST -H "Content-Type: application/json" -d '{"username":"John Doe", "password":"passwd", "savingAmount": 2000, "loanAmount":0}' localhost:5000/register
{
  "profile": "A"
}
```




