

@echo off
cmd /k "cd /d e:\at_pytest\ENV\Scripts & activate & cd /d e:\at_pytest\ & pytest -v --tb=line --alluredir=e:\at_pytest\Reports & cd /d e:\at_pytest\ & allure serve e:\at_pytest\Reports\"