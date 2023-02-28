# 爬虫的定时任务
service cron start
# 启动容器时，开启sshd
/usr/sbin/sshd -D &
# Django开启
nohup python3 /www/django_www/manage.py runserver 0.0.0.0:80 >> /www/django_www/django_www.log  2>&1

