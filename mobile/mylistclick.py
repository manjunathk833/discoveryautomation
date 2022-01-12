from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'Android',
    'deviceName': 'Redmi',
    'automationName': 'UiAutomator2',
    'appPackage': 'com.discovery.discoveryplus.mobile',
    'appActivity': 'com.discovery.plus.presentation.activities.LaunchActivity',
    'noReset': 'true'
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
try:
    wait = WebDriverWait(driver, 30)


    # Find the Free Trial Text
    wait.until(EC.presence_of_element_located((MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="My List"]/android.widget.ImageView'))).click()
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/sectionTitle')))
    time.sleep(1.0)



finally:
    driver.quit()