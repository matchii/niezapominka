# -*- coding: utf-8 -*-
from fabric.api import local
import re
from subprocess import call
import os

""" Buduje aplikację po zmianach. """
def build():
    local('python manage.py collectstatic --noinput')

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
    print("CREATE DATABASE `%s`;" % db_name)
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
        root_dir = local('pwd', capture=True)
    local("cat settings.example.py\
            | sed 's/$root_dir/%s/'\
            | sed 's/$db_name/%s/'\
            | sed 's/$db_user/%s/'\
            | sed 's/$db_password/%s/'\
            | sed 's/$db_host/%s/'\
            | sed 's/$db_port/%s/'\
            > settings.py" % (re.escape(root_dir), db_name, db_user, db_password, db_host, db_port))
    local('python manage.py syncdb')
    if not os.path.isdir('static'):
        local('mkdir static')
    build()
    print("\nWywołaj 'python manage.py runserver'.")
