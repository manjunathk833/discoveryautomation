from views.welcome_view import WelcomeView
from views.plans_picker_view import PlansView
from views.signin_view import SignInView
from utilities.customlogger import LogGen
from pytest_testrail.plugin import testrail, pytestrail


# driver object is instanciated by pytest wherever it is used, as parameter in this instance
@pytestrail.case('C1', 'C2')

# Test Case 3
def test_welcome_to_signin_navigation(driver):
    logger = LogGen().loggen()
    welcomescreen = WelcomeView(driver)

    # verify you're in the welcome screen
    logger.info("==================IN WELCOME SCREEN==========================")
    welcome_title_text = welcomescreen.verify_screen_title()
    assert welcome_title_text == 'Stream What You Love'

    logger.info("==================NAVIGATING TO SIGN IN SCREEN==========================")
    welcomescreen.nav_to_signin()

    signinscreen = SignInView(driver)
    email_text = signinscreen.verify_email_text()
    if email_text == 'EMAIL':
        logger.info("==================NAVIGATION TO SIGN IN SCREEN SUCCESSFUL==========================")
        assert True
    else:
        logger.error("==================NAVIGATION TO SIGN IN SCREEN FAILED==========================")
        driver.save_screenshot("screenshots\\" + "navtosignin.png")
        assert False

def test_exit(driver):
    logger = LogGen().loggen()
    welcomescreen = WelcomeView(driver)

    # verify you're in the welcome screen
    logger.info("==================VERIFYING WELCOME SCREEN==========================")
    welcome_title_text = welcomescreen.verify_screen_title()
    if welcome_title_text == 'Stream What You Love':
        logger.info("==================IN WELCOME SCREEN==========================")
        assert True
    else:
        logger.error("================== WELCOME SCREEN FAIL==========================")
        driver.save_screenshot("screenshots\\" + "welcomescreen.png")
        assert False
