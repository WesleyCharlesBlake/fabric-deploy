from os import path
import sys

from fabric.api import cd, env, hide,lcd, settings
from fabric.contrib import django
from fabric.contrib.files import exists
from fabric.operations import local, put, sudo, run, prompt, get


env.hosts = ['my.server.com']

dest_path = "/srv/www/django/data"
project_name = "ProjectName"
db_name = "database_name"

#get database from
def _pull_down_remote_db(): 
    dump_db_cmd = "ssh user@my.server.com \"sudo su - postgres -c 'pg_dump -E UTF-8 -T django_session %s' | gzip\" > %s.sql.gz" % (db_name,db_name)
    local_db_dump_path = "{}".format(path.join(dest_path, project_name))
    with settings(sudo_user='wesley'):
        with cd("/tmp"):
            print("Dumping database on remote..")
            run(dump_db_cmd)
        run('sudo mv /tmp/%s.sql.gz /srv/www/django/data/%s/' % (db_name,project_name))

def back_up():
    with cd("{}".format(path.join(dest_path, project_name))):
        _pull_down_remote_db()
    
    with cd("{}".format(path.join(dest_path))):
        sudo("tar -zcvf %s.tar.gz %s" % (project_name,project_name))
        print "Uploading the project archive - glacier-cmd will run"
        sudo("glacier-cmd upload old-sites %s.tar.gz --description '%s and DB back'" % (project_name,project_name))
