from views.browse_view import BrowseView

# driver object is instanciated by pytest wherever it is used, as parameter in this instance

# Test Case 1
def test_welcome_screen_elements(driver):

    # verify background image
    browsescreen = BrowseView(driver)
    browse_image_displayed = browsescreen.verify_network_image()
    if browse_image_displayed == True:
        assert True
    else:
        driver.save_screenshot("screenshots\\" + "welcomebgfailed.png")
        assert False
    # TODO validate the background image with reference image

    # Verify 'Discovery+' logo