from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # Find the Sign in Text
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/cta_button')))

    # Click Sign in Button
    start_watching_cta = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/cta_button')
    start_watching_cta.click()

    # Navigate to sign in page and find email text
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/cta_button')))
    watch_now_cta = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/cta_button')
    watch_now_cta.click()

    loader = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/loading_view_layout_id').is_displayed()
    assert loader == True

    subtitles = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/exo_subtitles').is_displayed()
    assert subtitles == True


finally:
    driver.quit()