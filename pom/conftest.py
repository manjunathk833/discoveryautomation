import pytest
from appium import webdriver

APPIUM = 'http://localhost:4723'
@pytest.fixture()
def driver():
    CAPS = {
        'platformName': 'Android',
        'deviceName': 'Redmi',
        'automationName': 'UiAutomator2',
        'appPackage': 'com.discovery.discoveryplus.mobile',
        'appActivity': 'com.discovery.plus.presentation.activities.LaunchActivity',
        'noReset': 'true'
    }

    # create a appium driver instance
    driver = webdriver.Remote(
        command_executor=APPIUM,
        desired_capabilities=CAPS
    )
    yield driver
    driver.quit()


import pytest


def pytest_sessionstart(session):
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result

def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')