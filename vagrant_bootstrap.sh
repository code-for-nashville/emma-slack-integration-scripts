#!/bin/bash

# Install git for version control, pip for install python packages
echo 'Installing pip...'
sudo apt-get update
sudo apt-get -y install python-pip

# install python packages
echo "Installing python packages and libs"
pip install ipdb
pip install pprintpp
pip install requests

# complete
echo ""
echo "Vagrant install complete."
echo "Now try logging in: vagrant ssh"
