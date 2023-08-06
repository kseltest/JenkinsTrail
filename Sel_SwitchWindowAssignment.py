from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

"""
switching windows 
a tags are for links 
"""


class Letskodeit:

    def __init__(self):
        self.url = "https://www.letskodeit.com/practice"
        self.driver = webdriver.Chrome()
        self.opentab_id_tag = "opentab"

    def browseletskodeit(self):
        """

        """
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(1)

    def browseCoursepage(self):
        """
        Clicking on the FAQ page url
        :return:
        """
        # prints the current URL and saves the current window id
        print("The current URL is : " + self.driver.current_url)
        present_window_handle = self.driver.current_window_handle
        print("Line 35 ----The current handle is : " + present_window_handle)

        # Clicking on faq page
        opentab_webelement = self.driver.find_element(By.ID, self.opentab_id_tag)
        opentab_webelement.click()
        sleep(1)
        opentab_webelement.click()
        sleep(1)
        opentab_webelement.click()

        # get all the active / availbale window handle
        all_window_handles = self.driver.window_handles
        print("Line 43 ---- Thelist of all windows is : ")
        print(all_window_handles)
        #
        for window_tab_code in all_window_handles:
            if (window_tab_code != present_window_handle):
                self.driver.switch_to.window(window_tab_code)
                sleep(10)
                print("The current URL after clicking is : " + self.driver.current_url)
                self.driver.close()
                #self.driver.quit()

                #break  #closes the current window
        #


obj = Letskodeit()
obj.browseletskodeit()
obj.browseCoursepage()
