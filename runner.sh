#!/usr/bin/env bash

pytest -v --tb=line --alluredir=/Reports ; allure serve /Reports