# -*- coding: utf-8 -*-
from fabric.api import local
import re
from subprocess import call
import os

""" Buduje aplikację po zmianach. """
def build():
    local('python manage.py collectstatic --noinput')
    if not os.path.exists('static/js/jquery.min.js'):
        local('cd static/js; ln -s jquery-1.6.4.min.js jquery.min.js')

"""
Buduje bazę. (Tak naprawdę, to nic nie buduje, bo do tego potrzebne są uprawnienia
na serwerze mysql. Wypisuje tylko zapytania, które trzeba wykonać.)
"""
def build_db(
        db_name="niezapominka",
        db_user='niezapominka',
        db_password='pass',
        db_host='localhost'
    ):
    print('Wykonaj poniższe zapytania aby utworzyć użytkownika i bazę:\n')
    print("CREATE DATABASE `%s` DEFAULT CHARACTER SET utf8 COLLATE utf8_polish_ci;" % db_name)
    print("CREATE USER '%s'@'%s' IDENTIFIED BY '%s';" % (db_user, db_host, db_password))
    print("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, INDEX, ALTER ON `%s`.* TO '%s'@'%s';" %
            (db_name, db_user, db_host)
    )

""" Buduje aplikację od zera. Wymaga ręcznego założenia użytkownika i bazy. """
def from_scratch(
        root_dir='',
        db_name="niezapominka",
        db_user='niezapominka',
        db_password='pass',
        db_host='localhost',
        db_port=''
    ):
    if (root_dir == ''):
        root_dir = re.escape(local('pwd', capture=True))
    else:
        root_dir = re.escape(root_dir)
    local("cat settings.example.py\
            | sed 's/$root_dir/%s/'\
            | sed 's/$db_name/%s/'\
            | sed 's/$db_user/%s/'\
            | sed 's/$db_password/%s/'\
            | sed 's/$db_host/%s/'\
            | sed 's/$db_port/%s/'\
            > settings.py" % (root_dir, db_name, db_user, db_password, db_host, db_port))
    local("cat django.example.wsgi | sed 's/$wsgi_path/%s/' > django.wsgi" % root_dir)
    local('python manage.py syncdb')
    if not os.path.isdir('static'):
        local('mkdir static')
    build()
    print("\nWywołaj 'python manage.py runserver'.")

def deploy_test():
    local('rsync -rl ./* /var/www/test/niezapominka/')
    #local('git archive master | tar -x -C /var/www/test/niezapominka/')
    #local('cd ../test/niezapominka; fab build')
