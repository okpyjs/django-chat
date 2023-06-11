# Django Chat APP

## How to use
### 1. install virtual environment and install dependencies
- Open terminal in root directory and Run below commands
```
py -m venv .venv
```
```
.venv\scripts\activate
```
```
pip install -r requirements.txt
```
### 2. Basic Setting
- Migrate
```
py manage.py makemigrations
```
```
py manage.py migrate
```
- Create super user
```
py manage.py createsuperuser
```
- Add users
Go to `localhost:8000/admin` and Login <br />
Go to http://localhost:8000/admin/auth/user/ <br />
Add user by clicking `ADD USER` button on right up corner <br />
Change user's `Staff status` to true by clicking `Staff status` checkbox
### 3. Test App
- Open serveral browsers <br />
- On each browser, follow below <br />
- Go to `localhost:8000/admin` and Login <br />
- Go to http://localhost:8000/chat/default/ <br />
- Enjoy

## Reference URL
[Introduction to Django Channels][reference]
[reference]: https://testdriven.io/blog/django-channels
