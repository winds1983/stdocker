#!/bin/bash

sudo rm -fr build/* dist/* stdocker.egg-info/*
python3 setup.py sdist bdist_wheel
twine upload --repository pypi dist/*

stdocker --version
