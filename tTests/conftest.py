import pytest
from selenium import webdriver
# from fixtures.driver import driver  # DO NOT DELETE fixture processing into tests
# from fixtures.pytesthtml import pytesthtml

base_url = "https://opensource-demo.orangehrmlive.com/"


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        # extra.append(pytest_html.extras.url(_current_url()))
        # report.extra = extra
        file_name = report.nodeid.replace("::", "_") + ".png"
#        driver.get_screenshot_as_file(str(file_name))
        print(item(self.current_url))

def _capture_screenshot(name):
    driver.get_screenshot_as_file(str(name))

def _current_url():
    driver.current_url()