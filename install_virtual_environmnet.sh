#!/usr/bin/env bash

if [ "$(whoami)" == "root" ]; then
    echo ""
    echo "You should not be running this script with sudo!"
    echo ""
    exit 1
fi

echo ""
echo ""
echo "Removing old virtual environment"
echo ""
echo ""
rm -rf venv

echo ""
echo ""
echo "Create virtual environment"
echo ""
echo ""
python3 -m venv --without-pip venv
source ./venv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate

echo ""
echo ""
echo "Install flask and dependencies into the virtual environment."
echo ""
echo ""
venv/bin/pip3 install flask
venv/bin/pip3 install gunicorn
venv/bin/pip3 install greenlet
venv/bin/pip3 install eventlet
venv/bin/pip3 install flask-socketio==1.0
