#!/bin/bash

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    sudo python3 -m venv env
fi

sudo chmod -R 777 env

source env/bin/activate

echo "Python virtual environment activated." 

pip3 install -r requirements.txt

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi
sudo chmod -R 777 logs
