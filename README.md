# scribe-app-demo

How to set up

Install Python 3.9.6 or above

From the folder scribe_app run 

```shell
pip3 -r requirements.txt
```
If that's not working run

```shell
pip -r requirements.txt
```

Do DB migrations

```shell
python3 manage.py makemigrations
```

```shell
python3 manage.py migrate
```

To start the app
```shell
python3 manage.py runserver
```


if above commands are not working try to use `python` instead of `python3`