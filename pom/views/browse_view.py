from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseView(object):
    #class variables

    # for network_image
    network_image = (MobileBy.XPATH, '//android.widget.FrameLayout[@content-desc="Browse"]/android.widget.ImageView')
    find_network_image = (MobileBy.XPATH,'//android.widget.FrameLayout[@content-desc="Browse"]/android.widget.ImageView')

    hgtv_icon = (MobileBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.ImageView')
    find_hgtv = (MobileBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.ImageView')

    def __init__(self, driver):
        self.driver = driver


    def verify_network_image(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.network_image))
        return self.driver.find_element(*self.find_network_image).is_displayed()

    def nav_to_browsepage(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.network_image))
        browsebutton = self.driver.find_element(*self.find_network_image).click()
        browsebutton.click()

    def verify_browsepage(self):
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located(self.network_image))
        return self.driver.find_element(*self.find_network_image).is_displayed()

    def nav_back(self):
        self.driver.back()


