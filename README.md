Django Inline Formset Example
=============================

Forked from:
https://github.com/epicserve/inlineformset-example


To start playing:

```bash
virtualenv env
source env/bin/activate

pip install -r config/requirements/dev.txt

./manage.py createsuperuser
# E.g.: admin/admin

./manage.py makemigrations
./manage.py migrate

./manage.py runserver
```

Test on the browser:
- http://localhost:8000/admin
- http://localhost:8000/


Cleaning up (assuming the virtual enrinoment is still active):
```bash
deactivate
# local folder env can also be deleted:
rm -rf env
```
