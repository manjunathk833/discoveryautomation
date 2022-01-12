from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInView(object):
    #class variables

    # for email
    email_text = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/signInEmailLabel')



    def __init__(self, driver):
        self.driver = driver

    def verify_email_text(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.email_text))
        emailtext = self.driver.find_element(*self.email_text)
        return emailtext.text