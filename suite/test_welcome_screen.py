
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#driver object is instanciated by pytest wherever it is used, as parameter in this instance
def test_welcome_screen(driver):
    # Create dynamic wait instance
    wait = WebDriverWait(driver, 20)


    # Full screen background image with gradient
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeBackground')))
    background_image = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeBackground').is_displayed()
    assert background_image == True
    # TODO validate the background image


    # 'Discovery+' logo
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeNetworkLogo')))
    logo = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeNetworkLogo').is_displayed()
    assert logo == True
    # TODO validate the Discovery logo



    # Screen title: "Stream What You Love
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeTitle')))
    welcome_title = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeTitle')
    welcome_title_text = welcome_title.text
    # validate that the proper text is displayed
    assert welcome_title.text == 'Stream What You Love'


    # description: "Your favorite brands and personalities plus exclusive originals, all in one place.
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeDescription')))
    welcome_description = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeDescription')
    welcome_description_text = welcome_description.text
    # validate that the proper text is displayed
    assert welcome_description_text == 'Your favorite brands and personalities plus exclusive originals, all in one place.'


    # onboarding message: "Watch X days free, then as low as $4.99/month."
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomePrice')))
    welcome_price = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomePrice')
    welcome_price_text = welcome_price.text
    # validate that the proper text is displayed
    # TODO report/fix below assertion
    #assert welcome_price_text == 'Watch 7 days free, then as low as $4.99.'


    # buttons: "Start X-Day Free Trial" and "Sign In
    wait.until(EC.presence_of_element_located((MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')))
    signin = driver.find_element(MobileBy.ID, 'com.discovery.discoveryplus.mobile:id/welcomeSignIn')
    signin_text = signin.text
    # validate that the proper text is displayed
    assert signin_text == 'Sign In'


