#!/usr/bin/env bash
pytest -s -v fTests.py --html=report.html --self-contained-html

"""
@pytest.mark.hookwrapper(autouse=True)
def pytesthtml(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="file:/E:/wm_front_web/tTests/screenshots/"{} alt="screenshot" style="width:600px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>'.format(file_name)
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
"""