#!/bin/bash

source env/bin/activate

echo "ENV is activated  "

export DEVELOPMENT_FLAG=local

echo "DEVELOPMENT_FLAG is set on Local "

cd /var/lib/jenkins/workspace/Python CI-CD Pipe Line

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic -- no-input

echo "Migrations done"

#cd /var/lib/jenkins/workspace/Python CI-CD Pipe Line

#sudo cp -rf gunicorn.socket /etc/systemd/system/
#sudo cp -rf gunicorn.service /etc/systemd/system/

#echo "$USER"
#echo "$PWD"



#sudo systemctl daemon-reload
#sudo systemctl start gunicorn

#echo "Gunicorn has started."

#sudo systemctl enable gunicorn

#echo "Gunicorn has been enabled."

#sudo systemctl restart gunicorn


#sudo systemctl status gunicorn

