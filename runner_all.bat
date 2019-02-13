

@echo off
cmd /k "cd /d D:\wm_front_web\ENV\Scripts & activate & cd /d D:\wm_front_web\ & pytest -v --tb=line --alluredir=D:\wm_front_web\Reports & cd /d D:\wm_front_web\ & allure serve D:\wm_front_web\Reports\"