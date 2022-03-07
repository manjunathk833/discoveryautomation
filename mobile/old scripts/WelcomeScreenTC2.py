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


    # Find the Free Trial Text
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeStartTrial')))


    # Click Free Trial Button
    free_trial_button = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeStartTrial')
    free_trial_button.click()


    # Find Choose your plan Text and verify that it is displayed
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/choose_your_plan')))
    choose_your_plan = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/choose_your_plan')
    choose_your_plan_text = choose_your_plan.text
    # validate that the proper text is displayed
    assert choose_your_plan_text == 'Choose Your Plan'

finally:
    driver.quit()