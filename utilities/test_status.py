from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TestStatus(SeleniumDriver):

    log = cl.custom_logging(logging.INFO)

    def __init__(self, driver):
        self.driver = driver
        super(TestStatus, self).__init__(driver)    # Passing the driver instance to parent/super class
        self.resultList = []

    def set_status(self, result, resultMessage):
        try:
            if result is True:
                self.resultList.append("PASS")
                self.log.info("*** Verification Successful : " + resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("*** Verification Failed : " + resultMessage)
                self.screenshot(resultMessage)
        except:
            self.resultList.append("FAIL")
            self.log.error("*** Exception Occurred")
            self.screenshot(resultMessage)

    def mark(self, result, resultMessage):
        self.set_status(result, resultMessage)

    def mark_final(self, testName, result, resultMessage):
        self.set_status(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + ": Test was Failed")
            self.resultList.clear()
            assert True == False    # To mark the test as failure
        else:
            self.log.info(testName + ": Test was Passed")
            self.resultList.clear()
            assert True == True     # To mark the test as success
