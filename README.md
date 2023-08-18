# Email-Campaign-Manager

### <p> 1. Add new user/subscriber </p>

#### Successful addition of user
<img width="1012" src="https://github.com/dhruv-goyal-10/Email-Compaign-Manager/blob/master/images/1.png">

#### If user already exists with the username an error will be thrown
<img width="1012" src="https://github.com/dhruv-goyal-10/Email-Compaign-Manager/blob/master/images/2.png">

#### If an active user exists with the email, an error will be thrown
<img width="1012" src="https://github.com/dhruv-goyal-10/Email-Compaign-Manager/blob/master/images/3.png">

### <p> 2. Unsubscribe the user using user_id </p>
###
#### If user exists with that user id, success message will be shown
<img width="1012" src="https://github.com/dhruv-goyal-10/Email-Compaign-Manager/blob/master/images/4.png">

#### Else an error will be thrown
<img width="1012" src="https://github.com/dhruv-goyal-10/Email-Compaign-Manager/blob/master/images/5.png">

### <p> 3. Add Campaigns </p>

### You can add or update existing campaigns via the Admin Panel

# SETUP

1. Clone the repository:

```CMD
git clone https://github.com/dhruv-goyal-10/Email-Compaign-Manager.git
```

To run the server, you need to have Python installed on your machine. If you don't have it installed, you can follow the instructions [here](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) to install it.

2. Install, Create and activate a virtual environment:

```CMD
pip install virtualenv
virtualenv venv
```

Activate the virtual environment

```CMD
source venv/bin/activate
```

3. Install the dependencies:

```CMD
pip install -r requirements.txt
```

4. Setup .env file in Email-Compaign-Manager/project

```
EMAIL_HOST_USER = ''
EMAIL_PORT = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST = ''
SECRET_KEY = ''
```

5.Run the migrate command

```CMD
python manage.py migrate
```

6. Run the backend server on localhost:

```CMD
python manage.py runserver
```

You can access the endpoints from your web browser following this url

```url
http://127.0.0.1:8000
```

7. You can create a superuser executing the following commands

```CMD
python manage.py createsuperuer
```

A prompt will appear asking for username followed by password.
To access the django admin panel follow this link and login through superuser credentials

```url
http://127.0.0.1:8000/admin/
```

8. Start the Celery worker (On a separate terminal with activated virtual environment):

```CMD
celery -A project.celery worker --pool=solo -l info
```


