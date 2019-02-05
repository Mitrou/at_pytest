import pytest
from fixtures.driver import driver  # DO NOT DELETE fixture processing into tests
# from fixtures.pytesthtml import pytesthtml

base_url = "https://opensource-demo.orangehrmlive.com/"




@pytest.mark.hookwrapper
def pytesthtml(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if 1 == 1: # (report.skipped and xfail) or (report.failed and not xfail):
        file_name = report.nodeid.replace("::", "_")+".png"
        _capture_screenshot(file_name)
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                   'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extra.append(pytest_html.extras.html(html))
    report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


@pytest.fixture(scope="session")
def driver(request):
    from selenium import webdriver
    web_driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",web_driver)
    yield
    web_driver.close()