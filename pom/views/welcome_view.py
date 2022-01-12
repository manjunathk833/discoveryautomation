from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WelcomeView(object):
    #class variables

    # for bgimage
    welcome_background_image = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeBackground')
    find_welcome_background_image = (MobileBy.ID,'com.discovery.discoveryplus.mobile:id/welcomeBackground')

    # for logo
    logo_image = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeNetworkLogo')
    find_logo_image = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeNetworkLogo')

    #for screen title
    screen_title = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeTitle')
    find_screen_title = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeTitle')

    #for welcome description
    welcome_description = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeDescription')
    find_welcome_description = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeDescription')

    #for welcome price
    welcome_price = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomePrice')
    find_welcome_price = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomePrice')

    # for sign in text
    signin_text = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')
    find_signin_text = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')

    # for freetrial button
    free_trial = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeStartTrial')
    find_free_trial = (MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeStartTrial')


    def __init__(self, driver):
        self.driver = driver


    def verify_background_image(self):
        wait = WebDriverWait(self.driver, 20)
        # Full screen background image with gradient
        wait.until(EC.presence_of_element_located(self.welcome_background_image))
        return self.driver.find_element(*self.find_welcome_background_image).is_displayed()

    def verify_logo_image(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.logo_image))
        return self.driver.find_element(*self.find_logo_image).is_displayed()

    def verify_screen_title(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.screen_title))
        welcome_title = self.driver.find_element(*self.find_screen_title)
        return welcome_title.text

    def verify_welcome_description(self):
        wait = WebDriverWait(self.driver, 20)
        #wait.until(EC.presence_of_element_located(self.welcome_description))
        welcome_desc = self.driver.find_element(*self.find_welcome_description)
        return welcome_desc.text

    def verify_welcome_price(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.welcome_price))
        welc_price = self.driver.find_element(*self.find_welcome_price)
        return welc_price.text

    def verify_signin_text(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.signin_text))
        signintext = self.driver.find_element(*self.find_signin_text)
        return signintext.text

    def nav_to_plan_picker(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.free_trial))
        free_trial_button = self.driver.find_element(*self.find_free_trial)
        free_trial_button.click()

    def nav_to_signin(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.signin_text))
        signin_button = self.driver.find_element(*self.find_signin_text)
        signin_button.click()

    def nav_back(self):
        self.driver.back()


