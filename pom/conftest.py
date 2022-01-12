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