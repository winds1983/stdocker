#!/bin/bash

# Uninstall old versions
# NOTE: Sometimes if we DO NOT remove old versions, the new package is cannot be installed
sudo pip3 uninstall -y stdocker

# Install local package
sudo python3 setup.py install

# Show version
stdocker --version
