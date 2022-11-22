#!/bin/bash

sudo cp -rf app.conf /etc/nginx/sites-available/app
sudo chmod 777 /var/lib/jenkins/workspace/python-ci-cd-testing

sudo ln -s /etc/nginx/sites-available/app /etc/nginx/sites-enabled
sudo nginx -t

sudo systemctl start nginx
sudo systemctl enable nginx

echo "Nginx has been started"

sudo systemctl status nginx
