from views.welcome_view import WelcomeView
from views.plans_picker_view import PlansView
from views.signin_view import SignInView
from utilities.customlogger import LogGen

# driver object is instanciated by pytest wherever it is used, as parameter in this instance

# Test Case 1
def test_welcome_screen_elements(driver):
    logger = LogGen().loggen()
    # verify background image
    logger.info("==================TESTCASE 1 STARTED==========================")
    welcomescreen = WelcomeView(driver)
    logger.info("==================VERIFYING WELCOME SCREEN==========================")
    background_image_displayed = welcomescreen.verify_background_image()
    if background_image_displayed == True:
        logger.info("==================BACKGROUND IMAGE PASSED==========================")
        assert True
    else:
        logger.error("==================BACKGROUND IMAGE FAILED==========================")
        driver.save_screenshot("screenshots\\" + "welcomebgfailed.png")
        assert False
    # TODO validate the background image with reference image

    logger.info("==================VERIFYING LOGO IMAGE==========================")
    # Verify 'Discovery+' logo
    logo_image_displayed = welcomescreen.verify_logo_image()
    if logo_image_displayed == True:
        logger.info("==================LOGO IMAGE PASSED==========================")
        assert True
    else:
        logger.error("==================LOGO IMAGE FAILED==========================")
        driver.save_screenshot("screenshots\\" + "welcomelogofailed.png")
        assert False
    # TODO validate the Discovery logo with reference image

    logger.info("==================VERIFYING STREAM TITLE TEXT==========================")
    # Verify Screen title: "Stream What You Love
    welcome_title_text = welcomescreen.verify_screen_title()
    if welcome_title_text == 'Stream What You Love':
        logger.info("==================STREAM TITLE TEXT FOUND==========================")
        assert True
    else:
        driver.save_screenshot("screenshots\\" + "welcomestreamtitle.png")
        logger.error("==================STREAM TITLE TEXT NOT FOUND==========================")
        assert False

    logger.info("==================VERIFYING WELCOME DESCRIPTION==========================")
    # verify description: "Your favorite brands and personalities plus exclusive originals, all in one place.
    welcome_description_text = welcomescreen.verify_welcome_description()
    if welcome_description_text == 'Your favorite brands and personalities plus exclusive originals, all in one place.':
        logger.info("==================WELCOME DESCRIPTION DISPLAYED CORRECTLY==========================")
        assert True
    else:
        logger.error("==================WELCOME DESCRIPTION FAILED==========================")
        driver.save_screenshot("screenshots\\" + "welcomedescription.png")
        assert False


    # onboarding message: "Watch X days free, then as low as $4.99/month."
    logger.info("==================VERIFYING WELCOME PRICE==========================")
    welcome_price_text = welcomescreen.verify_welcome_price()
    # TODO report/fix below assertion
    if welcome_price_text == 'Watch 7 days free, then as low as $5.99.':
        logger.info("==================WELCOME PRICE DISPLAYED CORRECTLY==========================")
        assert True
    else:
        # welcome_price_text_failed = driver.get_screenshot_as_base64()
        driver.save_screenshot("screenshots\\" + "welcomepricefailed.png")
        logger.error("==================WELCOME PRICE DETAILS FAILED==========================")
        assert False

    # buttons: "Start X-Day Free Trial" and "Sign In
    logger.info("==================VERIFYING WELCOME SCREEN SIGN IN BUTTON==========================")
    signin_text = welcomescreen.verify_signin_text()
    # validate that the proper text is displayed
    if signin_text == 'Sign In':
        logger.info("==================WELCOME SCREEN SIGN IN BUTTON DISPLAYED==========================")
        assert True
    else:
        logger.error("==================WELCOME SCREEN SIGN IN BUTTON FAILED==========================")
        driver.save_screenshot("screenshots\\" + "welcomesigninfailed.png")
        assert False


# Test Case 2
def test_welcome_to_plansview_navigation(driver):
    logger = LogGen().loggen()
    welcomescreen = WelcomeView(driver)

    # verify you're in the welcome screen
    logger.info("==================IN WELCOME SCREEN==========================")
    welcome_title_text = welcomescreen.verify_screen_title()
    assert welcome_title_text == 'Stream What You Love'

    logger.info("==================NAVIGATING TO PLANS PICKER SCREEN==========================")
    welcomescreen.nav_to_plan_picker()

    plansscreen = PlansView(driver)
    logger.info("==================VERIFYING NAVIGATION TO PLANS PICKER SCREEN==========================")
    plans_text = plansscreen.verify_choose_plan()
    if plans_text == 'Choose Youre Plan':
        logger.info("==================NAVIGATION FROM WELCOME TO PLANS PICKER SUCCESSFUL==========================")
        assert True
    else:
        logger.error("==================NAVIGATION FROM WELCOME TO PLANS PICKER FAILED==========================")
        driver.save_screenshot("screenshots\\" + "navtoplans.png")
        assert False


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


# Test Case 4
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

    logger.info("==================NAVIGATING BACK FROM WELCOME SCREEN==========================")
    welcomescreen.nav_back()
    logger.info("==================APP EXITED==========================")
