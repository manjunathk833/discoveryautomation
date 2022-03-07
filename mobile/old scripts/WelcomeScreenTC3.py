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
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')))

    # Click Sign in Button
    sign_in_button = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')
    sign_in_button.click()

    # Navigate to sign in page and find email text
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/signInEmailLabel')))
    email = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/signInEmailLabel')
    email_text = email.text

    # validate that the proper text is displayed
    assert email_text == 'EMAIL'
finally:
    driver.quit()