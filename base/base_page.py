from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging


class BasePage(SeleniumDriver):

    log = cl.custom_logging(logging.INFO)

    def __init__(self, driver):
        self.driver = driver

    def verify_page_title(self, expected_title):
        actual_title = self.getTitle()

        if actual_title == expected_title:
            self.log.info("Page Title Matched to :" + expected_title)
        else:
            self.log.info("Page Title Not Matched to :" + expected_title)


