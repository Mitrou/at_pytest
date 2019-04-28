#!/bin/bash


echo '### execution started ###'
git clone https://github.com/Mitrou/pyjenk

echo '### going into the folder cloned ###'
cd pyjenk

echo '#### Create Virtual Environment ####'
VIRTUAL_ENV_NAME='env'
virtualenv $VIRTUAL_ENV_NAME

echo '#### Activate Virtual Environment ####'
source $VIRTUAL_ENV_NAME/Scripts/activate

echo '#### Moving chromedriver to PATH ####'
cp chromedriver.exe $VIRTUAL_ENV_NAME/Scripts/activate

echo '#### Install requirements ####'
pip install -r requirements.txt

echo '#### Run tests ####'
pytest -v --tb=long --alluredir=allure-results
 
echo ### deactivate virtual environment ###
deactivate