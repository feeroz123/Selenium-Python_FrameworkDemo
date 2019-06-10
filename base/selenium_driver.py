from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from traceback import print_stack
import utilities.custom_logger as cl
import logging
import time
import os


class SeleniumDriver:

    log = cl.custom_logging(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.title

    def getBy(self, locator_type):
        locatorType = locator_type.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "partial_link":
            return By.PARTIAL_LINK_TEXT
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        else:
            self.log.error("*** The locator type ", locatorType, " is not valid")

        return False

    def waitForElement(self, locator, locator_type="id", timeoutSecs=7, poll_freq=1):
        element = None
        print("Waiting for the Element for max", timeoutSecs, "secs with polling frequency of", poll_freq, "secs..")
        wait = WebDriverWait(self.driver, timeout=timeoutSecs, poll_frequency=poll_freq,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        try:
            getby = self.getBy(locator_type)
            element = wait.until(EC.element_to_be_clickable((getby, locator)))
            self.log.info("Element was found with locator: ", locator)
        except:
            self.log.error("*** Element was not found with locator: ", locator)
        return element

    def isElementPresent(self, locator, locator_type="id", timeoutSecs=10, poll_freq=1):
        try:
            print("Waiting for the Element for max", timeoutSecs, "secs with polling frequency of", poll_freq, "secs..")
            wait = WebDriverWait(self.driver, timeout=timeoutSecs, poll_frequency=poll_freq,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            getby = self.getBy(locator_type)
            element = wait.until(EC.presence_of_element_located((getby, locator)))
            self.log.info("Element is present with locator: ", locator)
            return True
        except:
            self.log.error("*** Element is not present with locator: ", locator)
            return False

    def isElementDisplayed(self, timeoutSecs=7, poll_freq=1, element=None):
        try:
            print("Waiting for the Element display for max ", timeoutSecs, " secs with polling frequency of ", poll_freq, "secs..")
            wait = WebDriverWait(self.driver, timeout=timeoutSecs, poll_frequency=poll_freq,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            result = wait.until(EC.visibility_of_element_located(element))
            if result is not None:
                self.log.info("Element is displayed")
                return True
            else:
                self.log.error("*** Element is not displayed")
                return False
        except:
            self.log.error("*** Exception occurred while checking for element display")
            return False

    def clickElement(self, locator, locator_type="id"):
        try:
            element = self.waitForElement(locator, locator_type)
            element.click()
            self.log.info("Element was clicked with locator: '" + locator + "' and locator_type: " + locator_type)
        except:
            self.log.error("*** Element was not found with locator: '" + locator + "' and locator_type: " + locator_type)
            print_stack()

    def sendKeys(self, data, locator, locator_type="id"):
        try:
            element = self.waitForElement(locator, locator_type)
            element.send_keys(data)
            self.log.info("Keys were sent to element with locator: '" + locator + "' and locator_type: " + locator_type)
        except:
            self.log.error("*** Keys were not sent to element with locator: '" + locator + "' and locator_type: " + locator_type)
            print_stack()

    def screenshot(self, resultMessage):
        filename = resultMessage + "." + str(time.time() * 1000) + ".png"
        file_dir = "/screenshots/"
        full_file = file_dir + filename
        try:
            if not os.path.exists(file_dir):
                os.makedirs(file_dir)
            self.driver.save_screenshot(full_file)
            self.log.info("Screenshot saved as " + full_file)
        except:
            self.log.error("*** Exception while saving screenshot")
            print_stack()

    def scrollPage(self, direction="up"):
        if direction.lower() == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        elif direction.lower() == "half-up":
            self.driver.execute_script("window.scrollBy(0, -500);")
        elif direction.lower() == "half-down":
            self.driver.execute_script("window.scrollBy(0, 500);")
        elif direction.lower() == "little-up":
            self.driver.execute_script("window.scrollBy(0, -200);")
        elif direction.lower() == "little-down":
            self.driver.execute_script("window.scrollBy(0, 200);")
        else:
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_to_frame(self, frame_name):
        try:
            self.driver.switch_to.frame(frame_name)
            self.log.info("Switched to frame: " + frame_name)
        except:
            self.log.error("*** Exception occurred while switching to frame")

    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def select_dropdown_value(self, dropdown_locator, dropdown_locator_type="id", dropdown_value="India"):
        select = Select(self.waitForElement(dropdown_locator, dropdown_locator_type))
        try:
            select.select_by_visible_text(dropdown_value)
            self.log.info("Selected dropdown value as : " + dropdown_value)
        except:
            self.log.error("*** Dropdown Value not found: " + dropdown_value)




