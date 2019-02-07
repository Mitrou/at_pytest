-->still under construction!<--
## Repository for web test automation WM.

Browsers executables must be put into virtualenv/Scripts folder along with
Python.exe to avoid PATH issues. This is dependant on OS used. Current
implementation is done for Windows 10.

How to set up:
1. Install Python
2. Install virtualenv `pip install virtualenv`
3. Create virtualenv `virtualenv <virtual environment name>`
3. Activate virtualenv from CLI: `.\<env name>\Scripts\activate`
2. Execute in CLI from respective folder: `pip install -r requirements.txt` to install project libs
6. For Windows: execute following in MSPowerShell to install scoop (package manager for windows)
    6.1 `Set-ExecutionPolicy RemoteSigned -scope CurrentUser` to set rights
    6.2 `iex (new-object net.webclient).downloadstring('https://get.scoop.sh')'`
    6.3 Install allure framework(MSPowerShell): `scoop install allure`
    6.4 For other OSs please look into https://docs.qameta.io/allure/#_linux

How to run:
1. Build and execute CLI command from runners.sh (eg. `pytest -s -v -tb=line --alluredir=/tmp/my_allure_results`) under the respetive virtuanv activated.
    1.1 This will collect and execute tests. Also allure dfata would be stored.
2. Run allure report by `allure serve <report folder>` (eg. `allure serve /tmp/my_allure_results`)
    2.1 This will run web server with report page generated. Run history for each TC is supported. But real time update is not, sp you need to rerun allure serve after each test execution.

DoD:
- [x] Initial Structure
- [x] Reporting Engine
- [x] Some Smoke tests with FAILED reporting by trace and screenshot on failure
- [ ] Actual story test coverage


