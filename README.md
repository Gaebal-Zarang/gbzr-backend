# Gaebal-Zarang-backend

## Set-up requirement

- python version >= 3.10

## Setting steps

0. `pip install pyenv poetry`
1. `pyenv virtualenv (python-version) gbzr-backend` > create virtual-env
3. `pyenv local gbzr-backend` > set python-version in virtual-env

## Set-up steps

1. `pyenv shell gbzr-env`
2. `poetry shell` > activate virtualenv
3. `poetry update` or `poetry lock` > setting apply pyproject.toml
4. `python manage.py runserver` > start app
5. `python manage.py migrate` > for migration
6. `python manage.py createsuperuser` > create superuser(admin)

## Migration guide
