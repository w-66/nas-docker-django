service cron start

nohup python3 /www/django_www/manage.py runserver 0.0.0.0:80 >> /www/django_www/django_www.log  2>&1

