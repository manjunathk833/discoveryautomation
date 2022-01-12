from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlansView(object):
    #class variables

    # for choose your plan
    choose_your_plan = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/choose_your_plan')
    find_choose_your_plan = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/choose_your_plan')


    def __init__(self, driver):
        self.driver = driver

    def verify_choose_plan(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.choose_your_plan))
        plantext = self.driver.find_element(*self.find_choose_your_plan)
        return plantext.text