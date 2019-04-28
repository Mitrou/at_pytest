echo off

echo "### execution started ###"
git clone https://github.com/Mitrou/pyjenk

echo "### going into the folder cloned ###"
cd pyjenk

echo "#### Create Virtual Environment ####"
virtualenv env


cd env\Scripts\
activate & cd ..\.. & move chromedriver.exe env\Scripts\ & pip install -r requirements.txt & pytest -v --tb=long --alluredir=allure-results & deactivate









 

