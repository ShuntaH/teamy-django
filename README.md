# teamy-django

## How to setup
````
git clone git@github.com:ShuntaH/teamy-django.git

git submodule update -i

python3.8 -m venv venv

. venv/bin/activate.fish
# if using fish

pip install -r requirements.txt

python3.8 manage.py runserver 8001
````
## PyCharm
Setting

* Language & Framework -> Django

* Mark Enable Django

* Django Project Root -> project

* Settings -> project/project/settings.py

* Manage Script -> project/manage.py

Set Run Configuration
