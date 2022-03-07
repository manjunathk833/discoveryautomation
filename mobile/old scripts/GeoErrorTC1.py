from appium import webdriver
from os import path
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#CUR_DIR = path.dirname(path.abspath(__file__))
#APP = path.join(CUR_DIR, 'TheApp.apk')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Redmi',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.discovery.discoveryplus.mobile',
    'appActivity': 'com.discovery.plus.presentation.activities.LaunchActivity',
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/error_text')))
    geo_error = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/error_text')
    geo_error_text = geo_error.text
    assert geo_error_text == 'discovery+ is not yet available in this location.'


finally:
    driver.quit()