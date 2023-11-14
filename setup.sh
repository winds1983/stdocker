#!/bin/bash

sudo pip3 install -r requirements.txt

sudo pip3 install -U pip wheel setuptools twine

pip3 uninstall setuptools
sudo pip3 uninstall setuptools
sudo pip3 install setuptools==58.2.0
