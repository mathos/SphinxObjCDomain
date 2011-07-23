#!/bin/bash

sudo easy_install pip virtualenv

virtualenv --no-site-packages ~/sphinx_ext_env

source ~/sphinx_ext_env/bin/activate

pip install --upgrade -r requirements.txt

