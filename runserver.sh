#!/bin/bash

ROOTDIR=/scratch2/www/that/

. /scratch2/www/that/that_env/bin/activate

#python3 manage.py runserver 8861
uwsgi --plugin python3 --virtualenv $VIRTUAL_ENV --socket 127.0.0.1:8861 --chdir $ROOTDIR --wsgi-file $ROOTDIR/at/wsgi.py --logto $ROOTDIR/that.uwsgi.log --log-date --log-5xx --master --processes 4 --threads 2 --need-app 
