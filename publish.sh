#!/bin/bash

sudo rm -fr build/* dist/* stdocker.egg-info/*
sudo python3 setup.py sdist bdist_wheel
#sudo twine upload --repository pypi dist/*
python3 -m twine upload --repository pypi dist/*
